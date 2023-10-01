# extract_news.py
import os
from dotenv import load_dotenv
import requests
import pandas as pd

load_dotenv()

API_KEY = os.getenv("NEWS_APIKEY")

def get_all_news(query='*', from_date=None, to_date=None, language='en', page_size=100, page=1):
    """
    Fetch all news articles based on certain criteria from newsapi.org using the 'everything' endpoint.
    """

    base_url = "https://newsapi.org/v2/everything"
    parameters = {
        'apiKey': API_KEY,
        'q': query,
        'from': from_date,
        'to': to_date,
        'language': language,
        'pageSize': page_size,
        'page': page
    }

    all_articles = []
    total_results = 100 
    pages_to_fetch = total_results // page_size

    for page in range(1, pages_to_fetch + 1):
        parameters = {
            'apiKey': API_KEY,
            'q': query,
            'from': from_date,
            'to': to_date,
            'language': language,
            'pageSize': page_size,
            'page': page
        }
        response = requests.get(base_url, params=parameters)
        data = response.json()
        
        if data['status'] == 'ok':
            all_articles.extend(data['articles'])
        else:
            raise ValueError("API request failed. Reason:", data.get('message', "Unknown Error"))
        
        # If fewer articles are returned than expected, break out of loop
        if len(data['articles']) < page_size:
            break

    return pd.DataFrame(all_articles)

news_df = get_all_news(from_date='2023-10-01', to_date='2023-10-01', page_size=100)
news_df.to_csv('news_data.csv', index=False)