import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json, explode
from pyspark.sql.types import StructType, StructField, DoubleType, BooleanType, ArrayType,StringType,IntegerType

# Configuration Kafka
KAFKA_BROKER = "kafka:9092"
KAFKA_TOPIC = "stream_data"

# Création de la session Spark avec prise en charge de Hive
spark = SparkSession.builder \
    .appName("Kafka-Spark-Hive") \
    .config("spark.sql.catalogImplementation", "hive") \
    .config("spark.sql.warehouse.dir", "/user/hive/warehouse") \
    .config("hive.metastore.uris", "thrift://hive-metastore:9083") \
    .enableHiveSupport() \
    .getOrCreate()
#enableHiveSupport()!Permet à Spark de se connecter à Hive et d'exécuter des requêtes sur les tables Hive

# Vérification si la table Hive existe
try:
    spark.sql("DESCRIBE FORMATTED mental_health").show()
    print("La table 'mental_health' existe dans Hive.")
except Exception as e:
    print("Erreur : la table 'mental_health' n'existe pas ou Hive est inaccessible.")
    exit(1)

# Schéma des données Kafka
schema = StructType([
    StructField("User_ID", StringType(), True),
    StructField("Age", IntegerType(), True),
    StructField("Gender", StringType(), True), 
    StructField("Technology_Usage_Hours", DoubleType(), True),
    StructField("Social_Media_Usage_Hours", DoubleType(), True),
    StructField("Gaming_Hours", DoubleType(), True),
    StructField("Screen_Time_Hours", DoubleType(), True),
    StructField("Mental_Health_Status", StringType(), True),
    StructField("Stress_Level", StringType(), True),
    StructField("Sleep_Hours", DoubleType(), True),
    StructField("Physical_Activity_Hours", DoubleType(), True),
    StructField("Support_Systems_Access", StringType(), True),
    StructField("Work_Environment_Impact", StringType(), True),
    StructField("Online_Support_Usage", StringType(), True)
])

# Lecture du flux Kafka
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", KAFKA_BROKER) \
    .option("subscribe", KAFKA_TOPIC) \
    .load()

# Transformation des données
data = df.select(from_json(col("value").cast("string"), ArrayType(schema)).alias("data")) \
    .select(explode(col("data")).alias("record"))

# Filtrage des données nulles
clean_data = data.select("record.*").filter(
    col("User_ID").isNotNull() &
    col("Age").isNotNull() &
    col("Gender").isNotNull() &
    col("Technology_Usage_Hours").isNotNull() &
    col("Social_Media_Usage_Hours").isNotNull() &
    col("Gaming_Hours").isNotNull() &
    col("Screen_Time_Hours").isNotNull() &
    col("Mental_Health_Status").isNotNull() &
    col("Stress_Level").isNotNull() &
    col("Sleep_Hours").isNotNull() &
    col("Physical_Activity_Hours").isNotNull() &
    col("Support_Systems_Access").isNotNull()  &
    col("Work_Environment_Impact").isNotNull() &
    col("Online_Support_Usage").isNotNull()
)

# Écriture dans la table Hive avec insertInto
query = clean_data.writeStream \
    .outputMode("append") \
    .format("hive") \
    .option("checkpointLocation", "/tmp/spark_checkpoint") \
    .queryName("KafkaToHive") \
    .foreachBatch(lambda batch_df, batch_id: batch_df.write.insertInto("mental_health", overwrite=False))  # Insérer dans la table Hive

# Démarrer le streaming et attendre la fin
query.start().awaitTermination()
