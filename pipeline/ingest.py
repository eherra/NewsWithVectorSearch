import weaviate
import os
import pandas as pd
import numpy as np
from dotenv import load_dotenv

from pipeline.vector import TextVectorizer  # Assuming you have saved TextVectorizer class in vector.py

load_dotenv()

WEAVIATE_URL = os.getenv("WEAVIATE_DB_URL")
WEAVIATE_API_KEY = os.getenv("WEAVIATE_API_KEY")

auth_config = weaviate.AuthApiKey(api_key=WEAVIATE_API_KEY)

client = weaviate.Client(
    url=WEAVIATE_URL,
    auth_client_secret=auth_config
)

class Ingest:
    def __init__(self):
        self.vectorizer = TextVectorizer()  # Initialize the TextVectorizer

    def run(self, df):

        class_obj = {
            "class": "Article",
            "vectorizer": "none", # We provide our own embeddings
        }
        
        # Step 1: Read and process data
        df['text'] = df['title'] + " " + df['description']

        # Fill NaN values in the 'text' column
        df['text'].fillna("", inplace=True)

        if df.isnull().values.any():
            print("DataFrame contains NaN values!")

        # Step 3: Ingestion
        client.batch.configure(batch_size=100)
        with client.batch as batch:
            for _, row in df.iterrows():
                vector = self.vectorizer.encode([row["text"]])[0]  # Using the vectorizer
                vector = vector.numpy()  # Convert tensor to numpy array
                properties = {
                    "author": row["author"],
                    "title": row["title"],
                    "text": row["description"],
                    "date": row["publishedAt"],
                    "url": row["url"]
                }
                
                batch.add_data_object(
                    data_object=properties,
                    class_name="Article",
                    vector=vector
                )
