import weaviate
import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

WEAVIATE_URL = os.getenv("WEAVIATE_DB_URL")
WEAVIATE_API_KEY = os.getenv("WEAVIATE_API_KEY")

auth_config = weaviate.AuthApiKey(api_key=WEAVIATE_API_KEY)

client = weaviate.Client(
    url=WEAVIATE_URL,
    auth_client_secret=auth_config
)

class Ingest:
    def run(self, csv_path):
        # Read the data from the given path
        df = pd.read_csv(csv_path)

        # Ingestion to Weaviate
        client.batch.configure(batch_size=100)
        with client.batch as batch:
            for _, row in df.iterrows():
                print("ROWI ", row['vector'])  # log the vector

                properties = {
                    "author": row["author"],
                    "title": row["title"],
                    "text": row["text"]
                }
                batch.add_data_object(
                    data_object=properties,
                    class_name="Article",
                    vector=row["vector"]
                )
