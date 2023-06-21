## Desarrollo Sistema de Recomendación

<details>
  <summary>Tabla de contenido</summary>
  <ol>
    <li><a href="#Pipeline">Pipeline</a></li>
    <li><a href="#Tecnologías">Tecnologías Utilizadas</a></li>
    <li><a href="#Data Warehouse">Data Warehouse</a></li>
    <li><a href="#VertexAI">VertexAI</a></li>
    <li><a href="#Cloud Storage">Cloud Storage</a></li>
    <li><a href="#Deploy">Deploy</a></li>
  </ol>
</details>

## Pipeline
Para la creación del sistema de recomendación para usuarios de Yelp se siguió el flujo a continuación:

![pipeline](https://github.com/ksfajardo/PG-YELP-GMAPS/blob/main/src/RecSystem.png)

## Tecnologías
![Google Cloud](https://img.shields.io/badge/GoogleCloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
- scikit-surprise
- joblib
- Big Query
- Cloud Storage
- Cloud Run

## Data Warehouse
Los datos usados para el sistema de recomendación se extrajeron del Data Warehouse previamente conformado en el proceso de ETL, los datos a considerar en el desarrollo del modelo de machine learning, fueron los pertenecientes a las tablas business y Reviews de la base de datos Yelp.

![dwml](https://github.com/ksfajardo/PG-YELP-GMAPS/blob/main/src/bigqml.png)

## VertexAI
Para el desarrollo del modelo, se utilizó un Jupyter Notebook integrado en VertexAI, desde el cual se extrajeron los datos requeridos desde Big Query por medio de queries SQL y se asignaron a dataframes para poder trabajarse con pandas, scikit-learn y surprise. Se definió un modelo de recomendación para usuarios, usando el método SVD con filtro colaborativo, en el cual el usuario puede ingresar su ID de yelp y obtener 5 recomendaciones de diferentes restaurantes en base a su perfil y su similitud con otros perfiles. 
El modelo se entrenó y testeó con la métrica RMSE, además de haberse pasado por los métodos de Cross Validation y Grid Search para obtener los mejores hiperparametros. 

[Link al código del Notebook de VertexAI](https://github.com/ksfajardo/PG-YELP-GMAPS/blob/main/ML%20Model%20-%20API/modelyelp.ipynb) 

![vertexai](https://github.com/ksfajardo/PG-YELP-GMAPS/blob/main/src/Screenshot%202023-06-19%20220511.png)

## Cloud Storage
El modelo entrenado y los dataframes usados fueron exportados directamente desde el Workbench de VertexAI a un bucket de Cloud Storage para su posterior utilización en el deployment. 

![csml](https://github.com/ksfajardo/PG-YELP-GMAPS/blob/main/src/Screenshot%202023-06-19%20220407.png)

## Deploy
Para disponibilizar el sistema de recomendación al usuario, se creó una imagen de docker de los archivos en el bucket de Cloud Storage y el código necesario para hostear una API en FastAPI con un endpoint consumible que devuelva las recomendaciones hechas por el modelo cada vez que se llame y se le de un usuario existente en la base de datos de Yelp. 
Esta imagen de docker se utilizó dentro del servicio de Cloud Run para deployar online la API del modelo en FastAPI. 

[Link a la API deployada](https://yelp-rec-api-62b3ffvyva-uc.a.run.app) 

![depdocker](https://github.com/ksfajardo/PG-YELP-GMAPS/blob/main/src/dockerhim.png)
![depcrun](https://github.com/ksfajardo/PG-YELP-GMAPS/blob/main/src/WhatsApp%20Image%202023-06-20%20at%203.54.26%20PM.jpeg)
![apiml](https://github.com/ksfajardo/PG-YELP-GMAPS/blob/main/src/Screenshot%202023-06-15%20222511.png)

