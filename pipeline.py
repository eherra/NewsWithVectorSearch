import pandas as pd
import os
from pipeline.data_preparation import DataPreparation
from pipeline.vectorizer import Vectorizer
from pipeline.ingest import Ingest

from dotenv import load_dotenv
import weaviate
load_dotenv()

WEAVIATE_URL = os.getenv("WEAVIATE_DB_URL")
WEAVIATE_API_KEY = os.getenv("WEAVIATE_API_KEY")

auth_config = weaviate.AuthApiKey(api_key=WEAVIATE_API_KEY)

client = weaviate.Client(
    url=WEAVIATE_URL,
    auth_client_secret=auth_config
)

class Pipeline:
    def __init__(self, initial_csv_path):
        self.data_path = initial_csv_path
        self.dp = DataPreparation()
        self.vect = Vectorizer()
        self.ingest = Ingest()

    def run(self):
        # Step 1: Data Preparation
        processed_data_path = self.dp.run(self.data_path, "path_for_processed_data.csv")

        # Read and process data

        df = pd.read_csv(processed_data_path)

        df['text'] = df['title'] + " " + df['description']

        # Fill NaN values in the 'text' column
        df['text'].fillna("", inplace=True)

        # Step 2: Vectorization
        df['vector'] = list(self.vect.fit_transform(df['text']))


        vectorized_data_path = "path_for_vectorized_data.csv"

        df.to_csv(vectorized_data_path, index=False)
    
        print("Type: ", type(df['vector'].iloc[0])) 
        print("First ones: ", df['vector'].head())

        # Step 3: Ingestion
        self.ingest.run(vectorized_data_path)



if __name__ == "__main__":
    pipeline = Pipeline('/PATH_TO_CSV.csv')
    pipeline.run()