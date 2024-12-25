from dagster import asset, AssetExecutionContext, EnvVar
import pandas as pd
from pandas import DataFrame
import requests
import os


@asset(group_name='locations')
def get_locations(context: AssetExecutionContext) -> DataFrame:
    '''
    Get data from the list and return city long and lat with assigned city_id
    '''
    locations = []
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Referer': 'https://www.google.com',
    'DNT': '1',
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0'
}

    cities = ['An Giang', 
        'Ba Ria - Vung Tau', 'Bac Lieu', 'Bac Giang', 'Bac Kan', 'Bac Ninh', 
        'Ben Tre', 'Binh Duong', 'Binh Dinh', 'Binh Phuoc', 'Binh Thuan', 'Ca Mau', 'Cao Bang', 
        'Can Tho', 'Da Nang', 'Dak Lak', 'Dak Nong', 'Dien Bien', 'Dong Nai', 'Dong Thap', 'Gia Lai', 
        'Ha Giang', 'Ha Nam', 'Ha Noi', 'Ha Tinh', 'Hai Duong', 'Hai Phong', 'Hau Giang', 'Hoa Binh', 
        'Ho Chi Minh', 'Hung Yen', 'Khanh Hoa', 'Kien Giang', 'Kon Tum', 'Lai Chau', 
        'Lang Son', 'Lao Cai', 'Lam Dong', 'Long An', 'Nam Dinh', 'Nghe An', 'Ninh Binh', 'Ninh Thuan', 
        'Phu Tho', 'Phu Yen', 'Quang Binh', 'Quang Nam', 'Quang Ngai', 'Quang Ninh', 'Quang Tri', 
        'Soc Trang', 'Son La', 'Tay Ninh', 'Thai Binh', 'Thai Nguyen', 'Thanh Hoa', 'Thua Thien Hue', 
        'Tien Giang', 'Tra Vinh', 'Tuyen Quang', 'Vinh Long', 'Vinh Phuc', 'Yen Bai'
        ]
    if os.path.exists('./out/locations.csv'):
        context.log.info(f"File exists, skipping")
        return pd.read_csv('./out/locations.csv')

    for id, city in enumerate(cities):
        url = f"https://nominatim.openstreetmap.org/search?q={city},+Vietnam&format=json"
        context.log.info(f"Getting data for {city}")
        response = requests.get(url, headers=headers)
        response = response.json()
        
        location = {
            "city_id": id,
            "latitude": response[0]["lat"],
            "longitude": response[0]["lon"],
            "city": city,
        }

        locations.append(location)
    df = pd.DataFrame.from_records(locations)
    context.log.info(f"DataFrame:\n{df}")
    context.log.info(f"Number of rows: {len(df)}")
    df.to_csv(f'./out/locations.csv')
    return df