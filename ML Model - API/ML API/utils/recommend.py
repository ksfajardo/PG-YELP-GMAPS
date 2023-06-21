import numpy as np
import pandas as pd
import joblib
import surprise
import sklearn
from scipy import sparse

data_us=pd.read_parquet('data/data_us.parquet')
data_bus=pd.read_parquet('data/data_bus.parquet')

data_us['rating'] = data_us['rating'].astype(float)

modelo_yelp=joblib.load('data/modelo.joblib')

def get_recommendationyelp(usuario, data_us=data_us, data_bus=data_bus):
    rating = 4   # Tomamos películas a las que haya calificado con 4 o 5 estrellas
    df_user = data_us[(data_us['user_id'] == usuario) & (data_us['rating'] >= rating)]
    df_user = df_user.reset_index(drop=True)
    df_user= pd.merge(df_user, data_bus, on='business_id', how='inner')
    
    recomendaciones_usuario = data_bus.copy()
    usuario_vistas = data_us[data_us['user_id'] == usuario]
    
    recomendaciones_usuario = pd.merge(recomendaciones_usuario, usuario_vistas[['business_id']], how='left', indicator=True)
    recomendaciones_usuario = recomendaciones_usuario[recomendaciones_usuario['_merge'] == 'left_only']
    recomendaciones_usuario=recomendaciones_usuario.drop('_merge', axis=1)
    
    recomendaciones_usuario['Estimate_Score'] = recomendaciones_usuario['business_id'].apply(lambda x: modelo_yelp.predict(usuario, x).est)
    recomendaciones_usuario = recomendaciones_usuario.sort_values('Estimate_Score', ascending=False)
    recomendaciones= list(recomendaciones_usuario.local_name.head())
    return {'restaurantes recomendados': recomendaciones}
