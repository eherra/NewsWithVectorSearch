import os
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

class DataExtraction:
    
    API_KEY = os.getenv("NEWS_APIKEY")
    BASE_URL = "https://newsapi.org/v2/everything"

    def __init__(self):
        pass

    def get_all_news(self, query='*', from_date=None, to_date=None, language='en', page_size=100, page=1):
        """
        Fetch news articles based on certain criteria from newsapi.org using the 'everything' endpoint.
        """

        parameters = {
            'apiKey': self.API_KEY,
            'q': query,
            'from': from_date,
            'to': to_date,
            'language': language,
            'pageSize': page_size,
            'page': page
        }

        response = requests.get(self.BASE_URL, params=parameters)
        data = response.json()
        
        if data['status'] == 'ok':
            all_articles = data['articles']
        else:
            raise ValueError("API request failed. Reason:", data.get('message', "Unknown Error"))

        return pd.DataFrame(all_articles)

    def run(self, path):
        # Step 0: Data Extraction
        news_df = self.get_all_news(from_date='2023-10-01', to_date='2023-10-01', page_size=100)
        extracted_data_path = path
        news_df.to_csv(extracted_data_path, index=False)
        return extracted_data_path
