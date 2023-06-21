<p align='center'>
<img src ="src/DataVisualizationHeader.jpg" height=200>
<p>

## Índice 
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Contenido</summary>
  <ol>
    <li><a href="#Índice">Índice</a></li>
    <li><a href="#Contexto">Contexto</a></li>
    <li><a href="#Objetivo">Objetivo</a></li>
    <li><a href="#Alcance">Alcance</a></li>
    <li><a href="#transformación-de-datos-">Transformación de datos</a></li>
    <li><a href="#análisis-exploratorio-de-datos-eda-">EDA</a></li>
    <li><a href="#dashboard-">Dashboard</a></li>
    <li><a href="#stack-tecnológico">Stack Tecnológico</a></li>
    <li><a href="#warning-disclaimer">Disclaimer</a></li>
  </ol>
</details>

## Contexto

<p align="justify">
Recordaremos aquí el alcance del proyecto: el mismo está acotado por rubro de negocio, geográfica y temporalmente. 
Se trabajó sobre restaurantes de los cinco estados más poblados de los Estados Unidos (California, Texas, Florida, New York, Pennsylvania) con registros entre los años 2016 a 2021.

Nos ubicamos ahora en qué etapa del proyecto nos encontramos. Los datos ya se han pasado por los siguientes procesos: almacenamiento de archivos fuente en Cloud Storage, definición y ejecución de un proceso de ETL automatizado realizado en Cloud Functions, almacenamiento de las bases de datos resultante en Big Query.

Las bases de datos disponibilizadas en Big Query son GMaps, Places API y Yelp. La base de datos *`GMaps`* contiene dos tablas, *`metadata`* y *`reviews`*. Metadata contiene la información de los registros categorizados como restaurantes en el ETL y reviews contiene los comentarios de todos los negocios filtrados por los años correspondientes y de los cinco estados seleccionados. La base de datos *`Places API`* contiene dos tablas, *`business`* y *`reviews`*, con 1326 restaurantes nuevos y registros en reviews entre 2019 y 2023 (con un outlier de 2011). La base de datos de *`Yelp`* contiene tres tablas, *`business`*, *`reviews`* y *`checkin`*. La tabla business contiene la información de los registros categorizados como restaurantes que se encuentran en 3 de los 5 estados definidos en el alcance, reviews contiene los comentarios de los negocios filtrados por año y checkin los registros de los usuarios que estuvieron en un negocio sin filtrar.

</p>

<br/>

## Objetivo

La presente etapa tiene como objetivo desarrollar un dashboard interactivo que permita a los empresarios explorar los datos y extraer información relevante sobre los restaurantes.

Para lograr este objetivo, previo a la confección del dashborard, se realizaron análisis y visualizaciones que permitieron identificar patrones y tendencias de las características distintivas de los resturantes. Adicionalmente, con el fin de medir el progreso de la calidad, la cantidad e índole de los datos a tratar, se incluye el análisis de las dimensiones y propiedades de las bases de datos y la comparación de éstas.
 
El proyecto se desarrolla utilizando diferentes bibliotecas y herramientas de Python como Pandas, Matplotlib, Seaborn, Plotly y Dash.

<br/>

## Alcance

La presente sección tiene como objetivo presentar el análisis exploratorio de datos realizado sobre las bases de datos de Yelp y Google en relación a los restaurantes seleccionados. A continuación, se presentan las conclusiones más relevantes obtenidas.

<br/>

## Análisis Exploratorio sobre los datos de Yelp

- La mayoría de las calificaciones de los negocios en Yelp se encuentran en el rango de 3.5 a 5 estrellas.
- Los bares son los tipos de restaurantes más comunes en Yelp, seguidos por los restaurantes de tipo Pizza & Sandwich.
- Pensilvania tiene la mayor cantidad de restaurantes en el dataset de Yelp, seguido por Florida y California.
- Se observa una disminución en la cantidad de "checkins" a partir de 2020 debido a las restricciones por la pandemia.
- Las calificaciones en Yelp tienden a ser positivas, con una alta proporción de calificaciones de 4 y 5 estrellas.
- Los servicios de "takeout" y "delivery" son los más comunes en Yelp, y los restaurantes que ofrecen estos servicios junto con "dine-in" tienen un precio promedio más alto.

<br/>

## Análisis Exploratorio sobre los Datos de Google

- La mayoría de los registros en Google muestran calificaciones positivas, lo que indica una satisfacción general de los usuarios.
- Los bares son los tipos de restaurantes más comunes en Google, seguidos por los restaurantes para desayunos y los de comida internacional.
- La cantidad de comentarios en Google disminuyó en 2021 en comparación con 2019, posiblemente debido a la pandemia.
- Texas tiene menos restaurantes en comparación con su tamaño en comparación con Nueva York.
- Los restaurantes de comidas rápidas en Google reciben menos comentarios y tienen peores calificaciones en promedio.

<br/>

En resumen, este análisis exploratorio nos brinda información muy interesante sobre las calificaciones, los tipos de restaurantes, comentarios y servicios ofrecidos en Yelp y Google. Permite obtener insights sobre la satisfacción de los usuarios y las tendencias en la industria de restaurantes.

