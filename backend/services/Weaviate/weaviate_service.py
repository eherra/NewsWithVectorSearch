import weaviate
import json
from dotenv import load_dotenv
from os import getenv
load_dotenv()

WEAVIATE_URL = getenv("WEAVIATE_DB_URL")
WEAVIATE_API_KEY = getenv("WEAVIATE_API_KEY")

auth_config = weaviate.AuthApiKey(api_key=WEAVIATE_API_KEY)

client = weaviate.Client(
    url=WEAVIATE_URL,
    auth_client_secret=auth_config
)

def search_weaviate(userSearchInput, inputAsVector, alpha):
    """Fetches 10 most matching documents based on method parameters from Weaviate.
    
    Parameters:
        userSearchInput (str): User search query from the UI's text input.
        inputAsVector (str)  : Vectorized user search query.
        alpha (float)        : Float's of 1.0, 0.5 or 0.0 determining which search type to use.
                                - Vector search: 1.0
                                - Hybrid search: 0.5
                                - Text search:   0.0
    """
    response = (
        client.query
        .get("Article", ["title", "text", "author", "url", "date"])
        .with_additional(["score"])
        .with_hybrid(
            query=userSearchInput,
            vector=inputAsVector,
            #properties=["title", "text^2"], -> boosting text by 2
            alpha=alpha,
        )
        .with_limit(10)
        .do()
    )
    return json.dumps(response, indent=2)
