# Mise en place d’un data lake avec visualisation de données en utilisant Apache Kafka, Apache Spark, Apache Hive, Apache Druid et Power BI
 
## Description du Projet:
Le projet consiste à mettre en place un flux de données en temps réel pour l’analyse et la gestion des données liées à la santé mentale et à l’utilisation de la technologie. Il repose sur l’intégration de plusieurs technologies modernes, telles que FastAPI, Kafka, Apache Spark, Apache Druid et Power BI pour offrir une solution robuste permettant de collecter, traiter, analyser et visualiser des données issues de fichiers CSV.

L’objectif principal est de créer un système qui capte des données en temps réel, les nettoie et les stocke pour une analyse ultérieure. Ce système permet aux utilisateurs de comprendre les interactions entre la technologie et la santé mentale, en utilisant des agrégations et des visualisations de données.

Les étapes principales du projet incluent :

-Création d'un flux de données en temps réel : Utilisation de FastAPI pour diffuser un fichier CSV sous forme de flux JSON.
-Consommation et nettoyage des données : Utilisation de Kafka pour le streaming des données et de Spark pour leur consommation, nettoyage et stockage dans une base Hive.
-Analyse avec Apache Druid : Traitement des données avec Apache Druid pour effectuer des requêtes d’agrégation sur de grandes quantités de données.
-Visualisation des données avec Power BI : Exportation des données vers Power BI pour créer des visualisations interactives qui facilitent la prise de décisions basées sur les analyses.

## Architecture du Projet
