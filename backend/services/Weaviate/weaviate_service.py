import weaviate
import json
from os import getenv

WEAVIATE_URL = getenv("WEAVIATE_DB_URL")
WEAVIATE_API_KEY = getenv("WEAVIATE_API_KEY")

auth_config = weaviate.AuthApiKey(api_key=WEAVIATE_API_KEY)

client = weaviate.Client(
    url=WEAVIATE_URL,
    auth_client_secret=auth_config
)

def hybrid_search_weaviate(userSearchInput, inputAsVector):
    response = (
        client.query
        .get("Article", ["title", "text", "author"])
        .with_additional(["score"])
        .with_hybrid(
            query=userSearchInput,
            vector=inputAsVector,
            alpha=0.5,
        )
        .with_limit(3)
        .do()
    )
    return json.dumps(response, indent=2)
