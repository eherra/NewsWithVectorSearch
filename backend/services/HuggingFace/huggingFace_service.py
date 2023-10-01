import requests
from os import getenv

HUGGINGFACE_TOKEN = getenv("HUGGINGFACE_API_KEY")
model_id = "sentence-transformers/all-MiniLM-L6-v2"

api_url = f"https://api-inference.huggingface.co/pipeline/feature-extraction/{model_id}"
headers = {"Authorization": f"Bearer {HUGGINGFACE_TOKEN}"}

def create_embeddings_from_search_input(search_input):
    response = requests.post(api_url, headers=headers, json={"inputs": search_input, "options":{"wait_for_model":True}})
    return response.json()