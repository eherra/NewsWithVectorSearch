from flask import Flask, request, jsonify
from services.Weaviate import weaviate_service
from services.HuggingFace import huggingFace_service
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route("/ping")
def index():
    return "pong!"


@app.route("/api/search", methods=["POST"])
def search():
    input = request.get_json()
    search_input = input["searchInput"]
    search_input_vectorized = huggingFace_service.create_embeddings_from_search_input(search_input)
    data = weaviate_service.hybrid_search_weaviate(search_input, search_input_vectorized)
    return jsonify(data)