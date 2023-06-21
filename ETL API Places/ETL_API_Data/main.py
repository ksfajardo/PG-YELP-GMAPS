import pandas as pd
from pandas.io import gbq
from google.cloud import bigquery
from textblob import TextBlob
import functions_framework
import ast
import datetime

def hello_gcs(event, context):
    """Triggered by a change to a Cloud Storage bucket.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    def sentimentality(review):
            if review is None:
                return 'No message'
            else:
                sentiment = TextBlob(review).sentiment.polarity
                if sentiment > 0:
                    return 'Positive'
                elif sentiment < 0:
                    return 'Negative'
                else:
                    return 'Neutral'
    
    file_name = event['name']
    state=file_name.split('.')[0]

    business=pd.read_csv('gs://' + event['bucket'] + '/' + file_name)

    if state == 'California':
        business['state'] = 'CA'
    if state == 'NuevaYork':
        business['state'] = 'NY'
    if state == 'Pensilvania':
        business['state'] = 'PA'
    if state == 'Texas':
        business['state'] = 'TX'
    if state == 'Florida':
        business['state'] = 'FL'

    business['reviews'] = business['reviews'].apply(ast.literal_eval)
    business = business.explode('reviews')

    business.dropna(subset=['reviews'],inplace=True)
    business.reset_index(drop=True,inplace=True)

    nested_df = pd.DataFrame(business['reviews'].to_list())
    reviews = pd.concat([business['place_id'], nested_df], axis=1)
    reviews.drop(columns=['author_name','original_language','language','profile_photo_url','relative_time_description','translated'],inplace=True)

    reviews.drop_duplicates(inplace=True)
    reviews.reset_index(drop=True,inplace=True)

    reviews['time'] = reviews['time'].apply(lambda x: datetime.datetime.fromtimestamp(x).date())

    reviews['feeling'] = reviews['text'].apply(lambda x: sentimentality(x))

    business.drop_duplicates(subset=['place_id'],inplace=True)
    business.drop(columns=['address','reviews'], inplace=True)

    business = business.astype(str)
    reviews=reviews.astype(str)

    reviews.to_gbq(destination_table='PlacesAPI.' + 'reviews', 
                            project_id='pg-yelp-gmaps', 
                            table_schema=None,
                            if_exists='append', progress_bar=False,  auth_local_webserver=False,  location='us')
    
    business.to_gbq(destination_table='PlacesAPI.' + 'business', 
                            project_id='pg-yelp-gmaps', 
                            table_schema=None,
                            if_exists='append', progress_bar=False,  auth_local_webserver=False,  location='us')
