# Mise en place d’un data lake avec visualisation de données en utilisant Apache Kafka, Apache Spark, Apache Hive, Apache Druid et Power BI
 
## Description du Projet:
Le projet consiste à mettre en place un flux de données en temps réel pour l’analyse et la gestion des données liées à la santé mentale et à l’utilisation de la technologie. Il repose sur l’intégration de plusieurs technologies modernes, telles que FastAPI, Kafka, Apache Spark, Apache Druid et Power BI pour offrir une solution robuste permettant de collecter, traiter, analyser et visualiser des données issues de fichiers CSV.  

L’objectif principal est de créer un système qui capte des données en temps réel, les nettoie et les stocke pour une analyse ultérieure. Ce système permet aux utilisateurs de comprendre les interactions entre la technologie et la santé mentale, en utilisant des agrégations et des visualisations de données.  

Les étapes principales du projet incluent :  

-Création d'un flux de données en temps réel : Utilisation de FastAPI pour diffuser un fichier CSV sous forme de flux JSON.  
-Consommation et nettoyage des données : Utilisation de Kafka pour le streaming des données et de Spark pour leur consommation, nettoyage et stockage dans une base Hive.  
-Analyse avec Apache Druid : Traitement des données avec Apache Druid pour effectuer des requêtes d’agrégation sur de grandes quantités de données.  
-Visualisation des données avec Power BI : Exportation des données vers Power BI pour créer des visualisations interactives qui facilitent la prise de décisions basées sur les analyses.  
## Description du Dataset:
L'ensemble de données comprend des colonnes qui suivent l'utilisation quotidienne de la technologie et les indicateurs de santé mentale d'un individu. Voici ce qui est inclus :  

User_ID : identifiant unique pour chaque participant.  
Age : âge du participant.  
Daily_Screen_Time (heures) : temps d'écran quotidien moyen en heures.  
Mental_Health_Score (1-10) : score de santé mentale autodéclaré, où 1 est mauvais et 10 est excellent.  
Stress_Level (1-10) : niveau de stress autodéclaré, où 1 est très faible et 10 est très élevé.  
Sleep_Quality (1-10) : score de qualité du sommeil autodéclaré.

## Architecture du Projet
L'architecture du projet repose sur une approche modulaire qui combine plusieurs technologies et composants pour gérer le flux de données, leur traitement, et leur visualisation. Voici une vue d'ensemble de l'architecture :

### FastAPI (API RESTful) :

FastAPI sert de serveur pour exposer les données sous forme de flux JSON. Elle lit les données d'un fichier CSV (dans ce cas, mental_health_and_technology_usage_2024.csv) et les envoie sous forme de flux continu.
### Kafka (Système de messagerie) :

Kafka est utilisé pour gérer le flux de données en temps réel. Il sert de mécanisme de publication/abonnement où le producteur (FastAPI) publie les messages (données CSV) et le consommateur (Apache Spark) les consomme.  
Kafka dispose d'une interface graphique via Kafka UI pour surveiller et gérer les topics.
### Apache Spark (Traitement distribué) :

Apache Spark est utilisé pour consommer les messages provenant de Kafka, les nettoyer, effectuer des transformations et les stocker dans Hive pour un traitement ultérieur.
### Hive (Data Warehouse) :

Les données nettoyées et transformées par Spark sont stockées dans Hive. Hive agit ici comme un entrepôt de données pour les requêtes SQL sur de grandes quantités de données.
### Apache Druid (Stockage et analyse OLAP) :

Apache Druid est utilisé pour effectuer des analyses en temps réel sur les données stockées dans Hive. Druid offre une architecture orientée colonne, optimisée pour les requêtes analytiques rapides.  
Les données sont chargées depuis HDFS dans Apache Druid, et plusieurs requêtes analytiques sont exécutées pour extraire des informations utiles.
### Power BI (Visualisation) :

Les données traitées et analysées sont exportées vers Power BI pour la visualisation.  
Power BI permet de créer des rapports dynamiques, interactifs et des KPI basés sur les données stockées dans Hive et analysées par Druid.
## Exécution:
### Pré-requis:
Docker Desktop installé sur votre système  
```bash
docker --version
python est installé et en fonctionnement sur votre machine  
