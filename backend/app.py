from flask import Flask, request
from services.Weaviate import weaviate_service
from services.HuggingFace import huggingFace_service

app = Flask(__name__)

@app.route("/ping")
def index():
    return "pong!"


@app.route("/search", methods=["POST"])
def search():
    input = request.get_json()
    search_input = input["searchInput"]
    search_input_vectorized = huggingFace_service.create_embeddings_from_search_input(search_input)
    return weaviate_service.hybrid_search_weaviate(search_input, search_input_vectorized)