![header](https://github.com/ksfajardo/PG-YELP-GMAPS/blob/main/src/YELP%20%26%20GOOGLE%20MAPS%20-%20REVIEWS%20AND%20RECOMMENDATIONS.png)

## Índice
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Tabla de Contenidos</summary>
  <ol>
    <li><a href="#Índice">Índice</a></li>
    <li><a href="#Introducción">Introducción</a></li>
    <li><a href="#Objetivo">Objetivo</a></li>
    <li><a href="#Alcance">Alcance</a></li>
    <li><a href="#Tecnologías">Tecnologías utilizadas</a></li>
    <li><a href="#Pipeline">Pipeline</a></li>
    <li><a href="#Desarrolladores">Desarrolladores</a></li>
    <li><a href="#Metodología">Metodología</a></li>
  </ol>
</details>

## Introducción
En calidad de consultores de data, hemos sido contratados por un conglomerado de firmas gastronómicas de los Estados Unidos para llevar a cabo un análisis integral y brindar información valiosa para la toma de decisiones estratégicas.
El análisis se realiza en base a la información recopilada de dos plataformas populares, Yelp y Google Maps. Esta información comprende las opiniones de los usuarios en negocios de diversas categorías, así como las características asociadas a los mismos.
Con el fin de confeccionar un reporte con los hallazgos significativos se utilizaron diversas técnicas para el análisis de los comentarios y calificaciones de los usuarios. En este análisis se busca identificar la relación entre variables relevantes, tendencias y patrones en la industria gastronómica.
Por último, se desarrolló un sistema de recomendación de restaurantes para los usuarios de la plataforma Yelp.

## Objetivo
El objetivo general del proyecto es comprender la opinión de los clientes, identificar patrones de satisfacción y detectar factores clave que influyen en la calidad y éxito de dichos negocios.

## Alcance
Considerando el período establecido para el desarrollo del presente proyecto se decidió acotar el alcance del mismo en cuestiones de la industria objetivo, la fuente de datos, el alcance geográfico y el alcance temporal. El proyecto se enfoca en la industria gastronómica de los cinco estados más poblados de los Estados Unidos (California, Texas, Florida, New York, Pennsylvania) y se acota a los años entre 2016 y 2021, ya que son los años con datos más significativos considerando las fuentes seleccionadas, Google Maps y Yelp. Es importante destacar, que la industria seleccionada se basó en la variabilidad y relevancia de la misma en la economía estadounidense.

Análisis de definición de alcance: [Link](https://github.com/ksfajardo/PG-YELP-GMAPS/blob/main/EstadosTop5.ipynb)

## Tecnologías
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Google Cloud](https://img.shields.io/badge/GoogleCloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![Power Bi](https://img.shields.io/badge/power_bi-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Figma](https://img.shields.io/badge/figma-%23F24E1E.svg?style=for-the-badge&logo=figma&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white)
![Jira](https://img.shields.io/badge/jira-%230A0FFF.svg?style=for-the-badge&logo=jira&logoColor=white)
- Colab
- Deepnote
- seaborn
- scikit-surprise
- joblib
- TextBlob
- pyarrow

## Pipeline
![Pipeline](https://github.com/ksfajardo/PG-YELP-GMAPS/blob/main/src/Pipeline%20PGfondo.png)

- Diccionario de datos: [Link diccionario](https://docs.google.com/spreadsheets/d/1E0B0LYUlOoxMaXuXUV6i2kzVYoTtiZaH/edit?usp=sharing&ouid=110626938180094444619&rtpof=true&sd=true)
- Preprocesamiento de datasets más pesados y con errores: los datasets más grandes de yelp fueron fraccionados para más fácil procesamiento y prevención de errores - [Link Preprocesamiento](https://github.com/ksfajardo/PG-YELP-GMAPS/blob/main/ConversionArchivosParquet.ipynb)
- ETL de datasets Google Maps y Yelp: Proceso de extracción, transformación y carga de datos del Data Lake al Data Warehouse - [Link ETL Google Maps y Yelp](https://github.com/ksfajardo/PG-YELP-GMAPS/tree/main/GMaps_Yelp_ETL)
- ETL de nuevos datos de la API de Google Places: Obtención de nuevas fuentes de datos para complementar la información - [Link ETL API Places](https://github.com/ksfajardo/PG-YELP-GMAPS/tree/main/ETL%20API%20Places)
- Desarrollo de dashboard y KPIs: Desarrollo de dashboard interactivo con KPIs y análisis relevantes - [Link desarrollo Data Analytics](https://github.com/ksfajardo/PG-YELP-GMAPS/tree/main/DA)
- Desarrollo de sistema de recomendación: Desarrollo de sistema de recomendación para usuarios de la plataforma Yelp y deploy como una API - [Link desarrollo de sistema de recomendación](https://github.com/ksfajardo/PG-YELP-GMAPS/tree/main/ML%20Model%20-%20API),
	[Link deploy sistema de recomendación](https://yelp-rec-api-62b3ffvyva-uc.a.run.app)
  
## Desarrolladores
Pulsando sobre el nombre de cualquier integrante, serás redirigido a su respectivo perfil de Linkedin. 
  
</br>
  
<div align="center">
  
Data Engineering y Data Science:
| [<img src="https://avatars.githubusercontent.com/u/104804355?s=400&u=7c7592e2239f0ef414c4a3c5a61920ab19c9d980&v=4" width=115><br><sub>Karla Fajardo</sub>](https://www.linkedin.com/in/karla-fajardo-3b3020175/) | [<img src="https://avatars.githubusercontent.com/u/120281993?v=4" width=115><br><sub>Ariel Romero</sub>](https://www.linkedin.com/in/ariel-w-romero-a72514222/) |
  | :---: | :---: | 
  
</div>

<div align="center">

</br>
  
Data Analysis:
| [<img src="https://avatars.githubusercontent.com/u/95049464?v=4" width=115><br><sub>Paola Barrera</sub>](https://www.linkedin.com/in/pvbarrera93/) | [<img src="https://avatars.githubusercontent.com/u/95032482?v=4" width=115><br><sub>Mirta Julio</sub>](https://www.linkedin.com/in/mirta-gladys-julio-616895b/) | [<img src="https://avatars.githubusercontent.com/u/116127944?v=4" width=115><br><sub>Juan David Reyes</sub>](https://www.linkedin.com/in/juan-david-reyes-burbano-546a38262/) |
  | :---: | :---: | :---: |
  
</div>

## Metodología
  
<div align="center">
  
Diagrama de Gantt
  
![gant](https://github.com/ksfajardo/PG-YELP-GMAPS/blob/main/src/Gantt.png)

</div>
  
</br>
  
<div align="center">
  
Diagrama Metodología SCRUM
  
![scrum](https://github.com/ksfajardo/PG-YELP-GMAPS/blob/main/src/WhatsApp%20Image%202023-06-20%20at%208.37.31%20PM.jpeg)

</div>
  
