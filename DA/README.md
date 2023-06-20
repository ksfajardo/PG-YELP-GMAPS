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

Para lograr este objetivo, previo a la confección del dashborard, se realizaron análisis y visualizaciones que permitieron identificar patrones y tendencias de las características distintivas de los resturantes. Adicionalmente, con el fin de medir el progreso de la calidad, la cantidad e índole de los datos, se definieron cinco indicadores claves de rendimiento (KPIs):

+ Aumentar un 4% el número de calificaciones anualmente.
+ Disminuir un 4% el porcentaje de ratings negativos anualmente, considerando como ratings negativos valores de 1 y 2.
+ Aumentar un 4% el número de ratings con 5 estrellas anualmente.
+ Aumentar un 8% el número de opiniones con más de 30 caracteres anualmente para Google y con más de 200 caracteres para Yelp.
+ Aumentar un 3% el número de check in en Yelp trimestralmente.

Al monitorear estos KPIs a través del dashboard interactivo, los empresarios pueden obtener información valiosa y mejorar la toma de decisiones de negocio.

<br/>

## Alcance

### **`Transformación de datos`** 🔃✨

Realizado en el notebook `DA - Preprocesamiento` en Colab, en el mismo se procedió a eliminar registros que quedaron erróneamente dentro de la categoría restaurantes, completar los tres filtros definidos en la totalidad de los datos y a crear columnas con valores discretos de la información de cada restaurante.
En los datos provenientes de Google Maps y Yelp se procedió a extraer de la columna *`subcategory`* las categorías de los restaurantes establecidas en una función, el resultado se refleja en la columna *`rest_category`*. Adicionalmente, se crearon crearon las columnas *`abierto`* y *`service`*, las cuales reflejan los días abiertos en la semana y los servicios ofrecidos (*dine-in*, *delivery*, *takeout*), valores extríados de las columnas *`hours`*, *`MISC`* (Google) y *`attributes`* (Yelp). Por último, en el caso de Yelp, se creó una columna *`price`* que refleja el valor monetario relativo de cada restaurante, valores provenientes de la columna *`attributes`*.

Como información adicional, en la tabla *`metadata`* y *`business`* se crearon dos columnas: *`comment_2019`* y *`comment_2021`*, las cuales indican si en el restaurante correspondiente hubo al menos una calificación en el año correspondiente (indicado con 0 y 1).

### **`Análisis Exploratorio de Datos (EDA)`** 🔍📊📉

El `EDA` se realizó en un notebook de Deepnote utilizando las libreías Pandas, Matplotlib y Seaborn. Este análisis brinda información importante sobre las calificaciones, los tipos de restaurantes, comentarios y servicios ofrecidos en Yelp y Google. Adicionalmente, se obtienen insights sobre la satisfacción de los usuarios y las tendencias en la industria de restaurantes.

A continuación, se mencionan las conclusiones de mayor relevancia del análisis. Para los datos de Google Maps son:

+ La mayoría de los registros muestran calificaciones positivas, lo que indica una satisfacción general de los usuarios.
+ Los bares son los tipos de restaurantes más comunes, seguidos por los restaurantes para desayunos y los de comida internacional.
+ La cantidad de restaurantes con al menos una calificación por año disminuyó en 2021 en comparación con 2019, esto podría deberse al cierre de restaurantes debido a la pandemia.
+ Los restaurantes de comidas rápidas reciben menos comentarios y tienen peores calificaciones en promedio.

Las conclusiones proveniente de los datos de Yelp son:

+ La mayoría de las calificaciones de los negocios se encuentran en el rango de 3.5 a 5 estrellas.
+ Los bares son los tipos de restaurantes más comunes, seguidos por los restaurantes de tipo Pizza & Sandwich.
+ Pensilvania tiene la mayor cantidad de registros, seguido por Florida y California.
+ Se observa una disminución en la cantidad de "checkins" a partir de 2020 debido a las restricciones por la pandemia.
+ Las calificaciones en Yelp tienden a ser positivas, con una alta proporción de calificaciones de 4 y 5 estrellas.
+ Los servicios de "takeout" y "delivery" son los más comunes en Yelp, y los restaurantes que ofrecen estos servicios junto con "dine-in" tienen un precio promedio más alto.

### **`Dashboard`** 👨🏽‍💼👩‍💼💻📊

El dashboard se realizó en `Power BI`. El mismo contiene filtros temporales, por categoría de restaurante, por tipo de servicio ofrecido y, en el caso de Yelp, por tipo de precio. El dashboard muestra los `KPIs` previamente definidos, así como gráficas de barras, de línea, mapas y otros, que ayudan al entendimiento de los valores y variaciones de las variables definidas.

<br/>

## Stack Tecnológico

- Big Query
- Python
- Colab
- Deepnote
- Power BI

<img src="src/google_bigquery.png" width="150"/>
<img src="src/python_logo.png" width="150"/><img src="src/colab_logo.png" width="100"/><img src="src/deepnote_logo.png" width="170"/>
<img src="src/power_bi_logo.png" width="150"/>

<br/>

## :warning: Disclaimer

Este proyecto grupal fue desarrollado con fines de aprendizaje. Al explorar los contenidos de este repositorio, la información presentada y los resultados obtenidos **no debe** ser utilizada para la toma de decisiones reales.

