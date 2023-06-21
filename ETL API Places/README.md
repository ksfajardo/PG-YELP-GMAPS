## ETL de datos de Places API 

<details>
  <summary>Tabla de contenido</summary>
  <ol>
    <li><a href="#Pipeline">Pipeline</a></li>
    <li><a href="#Tecnologías">Tecnologías Utilizadas</a></li>
    <li><a href="#Extracción de datos con Cloud Functions">Extracción de datos con Cloud Functions</a></li>
    <li><a href="#Data Lake">Data Lake</a></li>
    <li><a href="#ETL automatizado con Cloud Functions">ETL automatizado con Cloud Functions</a></li>
    <li><a href="#Data Warehouse">Data Warehouse</a></li>
  </ol>
</details>

## Pipeline 
Como una segunda fuente de datos, se extrajeron los datos de los restaurantes de los cinco estados más poblados de Estados Unidos, a partir del año 2021. Se siguió el flujo a continuación:

![pipeline](https://github.com/ksfajardo/PG-YELP-GMAPS/blob/main/src/PipelAPI.png)

## Tecnologías
![Google Cloud](https://img.shields.io/badge/GoogleCloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
- Cloud Functions
- Cloud Storage
- Big Query

## Extracción de datos con Cloud Functions
Para extraer los datos, se creó una función en Cloud Functions(get_API_data) que por medio de una API Key, extrae los datos directamente desde la API de Google Places y devuelve un archivo csv con la información cada vez que se ejecuta la función, el cual exporta a Cloud Storage.

![getapidata](https://github.com/ksfajardo/PG-YELP-GMAPS/blob/main/src/getapidata.png)

## Data Lake
El archivo csv que resulta de la Cloud Function, se almacena en el Data Lake en Cloud Storage en un bucket aparte del que contiene la información de Google Maps y Yelp. 

![storageapi](https://github.com/ksfajardo/PG-YELP-GMAPS/blob/main/src/storageapiplaces.png)

## ETL automatizado con Cloud Functions
Como la información del csv se encuentra un poco desordenada y con algunas columnas anidadas, se desarrolló otra función en Cloud Functions(ETL_API_places) que se ejecuta cada vez que en el bucket respectivo se crea o modifica algún archivo y que se encarga de desanidar y cargar al Data Warehouse la información estructurada en sus respectivas tablas. 

![etlapi](https://github.com/ksfajardo/PG-YELP-GMAPS/blob/main/src/etlapidata.png)

## Data Warehouse
El proceso de ETL devuelve dos tablas, business y reviews, que se almacenan en el Data Warehouse en Big Query dentro de un schema llamado PlacesAPI, del cual se puede extraer la información con consultas SQL, conectándose al cliente de Big Query.

![bigqueryapi](https://github.com/ksfajardo/PG-YELP-GMAPS/blob/main/src/bqapiplaces.png)
