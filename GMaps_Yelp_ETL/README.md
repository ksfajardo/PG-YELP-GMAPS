## Desarrollo de ETL automatizado para los datasets de Google Maps y Yelp

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Tabla de contenido</summary>
  <ol>
    <li><a href="#Pipeline">Pipeline</a></li>
    <li><a href="#Tecnologías">Tecnologías Utilizadas</a></li>
    <li><a href="#Data Lake">Data Lake</a></li>
    <li><a href="#Cloud Function Automatizada">Cloud Function Automatizada</a></li>
    <li><a href="#Data Warehouse">Data Warehouse</a></li>
  </ol>
</details>

## Pipeline
Para el proceso de extracción, transformación y carga de los datos de este proyecto, se siguió el flujo a continuación:

![pipeline](https://github.com/ksfajardo/PG-YELP-GMAPS/blob/main/src/ETL_GMaps_Yelp.png)

## Tecnologías
![Google Cloud](https://img.shields.io/badge/GoogleCloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
- Cloud Storage
- Cloud Functions
- Big Query
- TextBlob

## Data Lake
El Data Lake se conformó en un bucket de Google Cloud Storage con los archivos en sus formatos originales, a excepción de los archivos business.pkl, review.json y user-002.parquet, los cuales sufrieron las siguientes transformaciones antes de ser cargados:
- business.pkl: Se arreglaron varias filas de la columna state que se encontraban desajustadas y se pasó el archivo a formato json. Se guardó en la carpeta Yelp en Cloud Storage.
- review.json: fue fraccionado en 46 partes, pasadas a formato parquet para facilitar su procesamiento. Se guardaron en review dentro de la carpeta Yelp en Cloud Storage.
- user-002.parquet: fue fraccionado en 14 partes, estas se mantuvieron el formato parquet. Se guardaron en user  dentro de la carpeta Yelp en Cloud Storage.

![datalakepng](https://github.com/ksfajardo/PG-YELP-GMAPS/blob/main/src/Storage.png)

</br>

<div align="center"> 
  
  ![datalakegif](https://github.com/ksfajardo/PG-YELP-GMAPS/blob/main/src/Storage.gif) 

</div>

## Cloud Function Automatizada
La transformación de los datos para pasarlos del Data Lake al Data Warehouse se hizo mediante una Cloud Function, la cual tiene como activador cualquier cargue o modificación al bucket en el que se encuentran almacenados, una vez se subieron los archivos a Cloud Storage, la función se ejecutó, haciendo las transformaciones necesarias para archivo y subiendolos después a sus respectivas tablas en el Data Warehouse. 

![cfuncpng](https://github.com/ksfajardo/PG-YELP-GMAPS/blob/main/src/Screenshot%202023-06-19%20210805.png)

</br>

<div align="center"> 

  ![cfuncgif](https://github.com/ksfajardo/PG-YELP-GMAPS/blob/main/src/ETL_Funcion.gif)

</div>

## Data Warehouse
La función anterior sube todos los datos transformados a tablas estructuradas en Big Query, el cual es un servicio que permite la conexión desde diversos medios y el acceso a los datos en las tablas por medio de queries SQL. Estos datos serán usados por los equipos de Data Analytics y Data Science según sus necesidades. 

![bigquerypng](https://github.com/ksfajardo/PG-YELP-GMAPS/blob/main/src/bigquery.png)

</br>

<div align="center"> 

  ![bigquerygif](https://github.com/ksfajardo/PG-YELP-GMAPS/blob/main/src/BigQuery.gif)

</div>
