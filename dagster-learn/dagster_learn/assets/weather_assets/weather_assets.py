from dagster import asset, AssetExecutionContext, EnvVar, MaterializeResult, MetadataValue, AssetIn, AssetKey
import pandas as pd
from pandas import DataFrame
import requests
from rich import print
import os
import numpy as np


from dagster_learn.assets.location_assets.location_assets import get_locations

@asset(ins={"locations": AssetIn(key="get_locations")}, group_name="weather")
def get_weather_data(context: AssetExecutionContext, locations) -> MaterializeResult:
    '''
    Get weather data from the open-meteo API and return it as a DataFrame
    '''
    # locations = pd.read_csv('./out/locations.csv',nrows=10)
    weather_data = []
    locations = locations.head(10)
    for _, location in locations.iterrows():
        url = f"https://api.open-meteo.com/v1/forecast?latitude={location['latitude']}&longitude={location['longitude']}&current_weather=true&timezone=auto"
        response = requests.get(url).json()
        weather = {
            "city_id": location['city_id'],
            "city": location['city'],
            "temperature": response['current_weather']['temperature'],
            "windspeed": response['current_weather']['windspeed'],
            "winddirection": response['current_weather']['winddirection'],
            "weathercode": response['current_weather']['weathercode'],
            "time": response['current_weather']['time'],
        }
        weather_data.append(weather)
        context.log.info(f"Got weather data for {location['city']}")
    df = pd.DataFrame.from_records(weather_data)
    # context.log.info(f"DataFrame:\n{df.head()}")
    # context.log.info(f"Number of rows: {len(df)}")
    df.to_csv(f'./out/weather.csv', index=False)
    return MaterializeResult(
        metadata={
            "num_records": len(df),
            "preview": MetadataValue.md(
                df.head().to_markdown()
            )
        }
    )


@asset(deps=['get_weather_data'], group_name="weather")
def temperature_level(context: AssetExecutionContext) -> MaterializeResult:
    df = pd.read_csv('./out/weather.csv')

    df['tempature_level'] = np.where(
        df['temperature'] < 10, 'low', 
        np.where(
            (df['temperature'] >= 10) & (df['temperature'] < 20), 'medium', 'high'
        )
    )

    return MaterializeResult(
        metadata={
            "num_records": len(df),
            "preview": MetadataValue.md(
                df.head().to_markdown()
            )
        }
    )


def get_pollution_data(lat: float, lon: float, start_time: int=None, end_time: int=None):
    '''
    Get data based on long and lat with start and end datetime
    '''
    api_endpoint = "https://api.openweathermap.org/data/2.5/air_pollution"

    res = requests.get(
        api_endpoint,
        params={
            "lat": lat,
            "lon": lon,
            # "start": start_time,
            # "end": end_time,
            "appid": os.getenv('API_KEY'),
        },
    )
    data = res.json()
    return data

@asset(deps=['get_locations'], group_name="weather")
def get_popullation(context: AssetExecutionContext):
    get_locations = pd.read_csv('./out/locations.csv')
    locations = get_locations.head(10)

    df_out = pd.DataFrame()
    for _, row in locations.iterrows():
        city_name = row['city']

        metrics = get_pollution_data(lat = row['latitude'], lon = row['longitude']) 
        print(metrics)
        metrics['city_id'] = row['city_id']
        df = pd.json_normalize(metrics, "list", [["coord", "lon"], ["coord", "lat"], 'city_id'])
        df_out = pd.concat([df_out, df], ignore_index=True)
        context.log.info(f"Getting data for {row['city']}")
        
        context.log.info(f"Got data for {row['city']}")
    df_out.to_csv('./out/pollution.csv')
    return MaterializeResult(
        metadata={
            "num_records": len(df_out),
            "preview": MetadataValue.md(
                df_out.head().to_markdown()
            )
        }
    )

    
    