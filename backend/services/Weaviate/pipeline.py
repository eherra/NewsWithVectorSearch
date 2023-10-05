import weaviate
import json
import requests
#from ..HuggingFace import huggingFace_service
from os import getenv
from dotenv import load_dotenv
load_dotenv()

WEAVIATE_URL = getenv("WEAVIATE_DB_URL")
WEAVIATE_API_KEY = getenv("WEAVIATE_API_KEY")

auth_config = weaviate.AuthApiKey(api_key=WEAVIATE_API_KEY)

client = weaviate.Client(
    url=WEAVIATE_URL,
    auth_client_secret=auth_config
)

class_obj = {
    "class": "Article",
    "vectorizer": "none", # We provide our own embeddings
}

#client.schema.delete_class("Article")
#client.schema.create_class(class_obj)

mock_file = open('news_mock.json') # mock data for testing
data = json.load(mock_file)

client.batch.configure(batch_size=100)
with client.batch as batch:
    for i, d in enumerate(data): 
        print(f"importing articles: {i+1}")
        properties = {
            "author": d["author"],
            "title": d["title"],
            "text": d["text"],
        }
        # generate vectors from Article's text
        #article_text_as_vectors = create_embeddings_from_search_input(d["text"])
        batch.add_data_object(
            data_object=properties,
            class_name="Article",
            #vector=article_text_as_vectors
        )

mock_file.close()