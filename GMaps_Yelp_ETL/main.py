import pandas as pd
from pandas.io import gbq
from google.cloud import bigquery
from textblob import TextBlob
import functions_framework
import json

def hello_gcs(event, context):
    """Triggered by a change to a Cloud Storage bucket.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    
    food_service= ['restaurant','cafe', 'food','pub','bar','coffee','breakfast','brunch','bakery','sandwich','ice cream','gastropubs']

    def sentimentality(review):
            if review is None:
                return 'No message'
            else:
                feel = TextBlob(review).sentiment.polarity
                if feel > 0:
                    return 'Positive'
                elif feel < 0:
                    return 'Negative'
                else:
                    return 'Neutral'

    def clean_category(category):
        return ', '.join(category)  

    #Obteniendo ruta de archivo modificado y tipo de archivo
    file_name = event['name']
    file_type = file_name.split('.')[-1]

    if '/' in file_name:
        main_folder = file_name.split('/')[0]
        last_folder = file_name.split('/')[file_name.count('/')-1]
        
        if main_folder == 'GMaps':
            dataset = 'GMaps.'
            if file_name.split('/')[1] == 'reviews-estados':
              table_name = 'Reviews'
              state = last_folder.split('-')[-1]
            if file_name.split('/')[1] == 'metadata-sitios':
              table_name = 'Metadata'
       
        if main_folder == 'Yelp':
            dataset = 'Yelp.'
            if last_folder == 'review':
                table_name = 'Reviews'
            elif last_folder=='user':
                table_name= 'Users'
            else:
                table_name = file_name.split('.')[0].split('/')[1]
    
        # Revisando si archivo es csv
    if file_type == 'csv':
        # Leyendo archivo en dataframe
        data = pd.read_csv('gs://' + event['bucket'] + '/' + file_name)

        # Revisando si archivo es json    
    if file_type == 'json':
        try:
            # Intentar leer el archivo json como si no tuviera saltos de linea
            data = pd.read_json('gs://' + event['bucket'] + '/' + file_name)
        except ValueError as e:
            if 'Trailing data' in str(e):
                # Leer el archivo json conteniendo saltos de linea
                data = pd.read_json('gs://' + event['bucket'] + '/' + file_name, lines = True)
            else:
                # Cualquier otro error
                print('Ocurrió un error cargando el archivo JSON:', e)
        
        # Revisar si el archivo es tipo parquet
    if file_type == 'parquet':
        # Leyendo archivo en dataframe
        data = pd.read_parquet('gs://' + event['bucket'] + '/' + file_name)
    
    #Google Maps
    if main_folder == 'GMaps':
        if 'review' in last_folder:
            data['user_id'] = data['user_id'].astype(str)
            data.drop(columns=['name','pics','resp'],inplace=True)
            data.rename(columns={'text':'opinion', 'time':'date'}, inplace=True)
            data['date'] = pd.to_datetime(data['date'], unit='ms').dt.strftime('%Y-%m-%d')
            data['date'] = pd.to_datetime(data['date'], format='%Y-%m-%d')
            data = data[data['date'].dt.year >= 2016]
            data.drop_duplicates(inplace=True)
            data['feeling'] = data['opinion'].apply(lambda x: sentimentality(x))
              
            if state == 'California':
                data['state'] = 'CA'
            if state == 'New_York':
                data['state'] = 'NY'
            if state == 'Pennsylvania':
                data['state'] = 'PA'
            if state == 'Texas':
                data['state'] = 'TX'
            if state == 'Florida':
                data['state'] = 'FL'

        if last_folder == 'metadata-sitios':
            data['platform']='Google Maps'
            data.drop(columns=['relative_results','address','url','description'],inplace=True)
            data.rename(columns={'name':'local_name','category':'subcategory'}, inplace=True)
            data['subcategory'] = data.apply(lambda row: clean_category(row['subcategory']) if isinstance(row['subcategory'], list) and row['subcategory'] else 'No category assigned', axis=1)
            data['subcategory'] = data['subcategory'].str.lower()
            data['category'] = 'other'
            data['category'] = data['subcategory'].apply(lambda x: 'food service' if x and any(word in x for word in food_service) else 'other')
            data=data[data['category']=='food service']
            data = data.applymap(lambda x: json.dumps(x) if isinstance(x, (list, dict)) else x)
            data.drop_duplicates(inplace=True)
            data.reset_index(drop=True,inplace=True)

    # Yelp
    if main_folder == 'Yelp':
        if  last_folder == 'review':
            data.drop(columns=['cool','funny','useful'], inplace=True)
            data.rename(columns={'text':'opinion', 'stars':'rating'}, inplace=True)
            data['date'] = pd.to_datetime(data['date']).dt.strftime('%Y-%m-%d')
            data['date'] = pd.to_datetime(data['date'], format='%Y-%m-%d')
            data = data[data['date'].dt.year >= 2016]
            data['feeling'] = data['opinion'].apply(lambda x: sentimentality(x))

        if table_name == 'business':
            states = ['TX', 'CA', 'PA', 'NY', 'FL']
            data['platform'] = 'Yelp'
            data = data[data['state'].isin(states)]
            data.drop(columns=['address','postal_code','is_open','city'], inplace=True)
            data.rename(columns={'name':'local_name', 'review_count':'num_of_reviews','categories':'subcategory'}, inplace=True)
            data['subcategory'].fillna('No category assigned', inplace=True)
            data['subcategory'] = data['subcategory'].str.lower()
            data['category'] = 'other'
            data['category'] = data['subcategory'].apply(lambda x: 'food service' if x and any(word in x for word in food_service) else 'other')
            data=data[data['category']=='food service']
            data = data.applymap(lambda x: json.dumps(x) if isinstance(x, (list, dict)) else x)
            data.drop_duplicates(inplace=True)
            data.reset_index(drop=True,inplace=True)
        
        if last_folder == 'user':
            data.drop(columns=['name','yelping_since','funny','cool','elite','fans','average_stars','compliment_hot','compliment_more','compliment_profile','compliment_cute','compliment_list','compliment_note','compliment_plain','compliment_cool','compliment_funny','compliment_writer','compliment_photos'],inplace=True)
            data.rename(columns={'review_count':'num_of_reviews'}, inplace=True)

        if table_name == 'tip':
            data.rename(columns={'text':'opinion'}, inplace=True)
            data['feeling'] = data['opinion'].apply(lambda x: sentimentality(x))

    data = data.astype(str)
    
    data.to_gbq(destination_table=dataset + table_name, 
                            project_id='pg-yelp-gmaps', 
                            table_schema=None,
                            if_exists='append', progress_bar=False,  auth_local_webserver=False,  location='us')