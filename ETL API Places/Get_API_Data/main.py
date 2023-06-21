import os
import requests
from flask import jsonify
from google.cloud import storage
import json
import random
import pandas as pd

# Una función aleatoria se agrega para cambiar un poco la longitud y la latitud y obtener resultados diferentes
def get_random_offset():
    return random.uniform(-0.01, 0.01)

def search_restaurants(request):
    locations = {
        "California": ["San Mateo","San Francisco", "Los Angeles", "San Diego", "Sacramento", "Santa Clara", "Fresno","Alameda", "Orange","Kern","Riverside", "San Joaquin","Contra Costa","Ventura"],
        "Texas": ["Harris","Dallas","Tarrant","Bexar","Travis","Collin","Denton","Hidalgo"," El Paso","Fort Bend","Montgomery","Williamson","Cameron","Nueces"],
        "Florida":["Miami-Dade","Broward","Palm Beach","Hillsborough","Orange","Pinellas","Duval","Lee","Polk","Brevard","Volusia","Pasco","Seminole","Sarasota"],
        "NuevaYork":["Kings","Queens","New York","Bronx","Richmond","Suffolk","Nassau","Westchester","Erie","Monroe","Onondaga","Orange","Rockland","Albany"],
        "Pensilvania":["Philadelphia","Allegheny","Delaware","Montgomery","Bucks","Lehigh","Lancaster","Chester","Northampton","Dauphin","Erie","Luzerne","York","Westmoreland"]
    }
    api_key = 'AIzaSyDtGhV7VvenzQClmkjwUCarIEVGrdXA7Ug'

    for state, cities in locations.items():
        random.shuffle(cities)  # reorganiza las ciudades
        restaurant_data = []
        for city in cities:
            # se obtienen las coordenadas de la ciudad
            geocoding_url = f'https://maps.googleapis.com/maps/api/geocode/json?address={city},{state}&key={api_key}'
            geocoding_response = requests.get(geocoding_url)
            geocoding_result = geocoding_response.json().get('results', [])
            if geocoding_result:
                location_lat = geocoding_result[0]['geometry']['location']['lat'] + get_random_offset()
                location_lng = geocoding_result[0]['geometry']['location']['lng'] + get_random_offset()
            else:
                # Manejar el caso en el que no se encuentren resultados de geocodificación
                # Puedes imprimir un mensaje de error o tomar alguna otra acción
                continue

            # parámetros de búsqueda
            query = 'restaurant'
            radius = 50000
            fields = 'name,rating,formatted_address,geometry,reviews'

            # buscamos con las coordenadas los restaurantes dentro de 50 km
            url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location_lat},{location_lng}&radius={radius}&type={query}&key={api_key}'

            # realizamos la solicitud y obtenemos los resultados
            response = requests.get(url)
            results = response.json().get('results', [])

            # para cada resultado, obtenemos los detalles necesarios
            for result in results:
                place_id = result['place_id']
                details_url = f'https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&fields={fields}&key={api_key}'
                details_response = requests.get(details_url)
                details = details_response.json().get('result', {})

                # Obtenemos los datos requeridos y los agregamos al diccionario
                restaurant = {
                    'name': details.get('name', ''),
                    'rating': details.get('rating', 'N/A'),
                    'address': details.get('formatted_address', ''),
                    'latitude': details['geometry']['location'].get('lat', ''),
                    'longitude': details['geometry']['location'].get('lng', ''),
                    'reviews': details.get('reviews', []),
                    'place_id': place_id
                }
                restaurant_data.append(restaurant)

        # el JSON se aplana
        df = pd.json_normalize(restaurant_data)

        # convertimos los datos en un diccionario
        restaurant_data_flat = df.to_csv(index=False)
    

        # Guardar archivo JSON
        storage_client = storage.Client()
        bucket_name = 'api-data-places'
        bucket = storage_client.get_bucket(bucket_name)
        destination_blob_name = f'{state}.csv'
        blob = bucket.blob(destination_blob_name)
        blob.upload_from_string(restaurant_data_flat, content_type='text/csv')

    return 'Done'
