from flask import Flask, request, jsonify, render_template
from services.Weaviate import weaviate_service
from services.HuggingFace import huggingFace_service
from flask_cors import CORS

app = Flask(
    __name__,
    static_url_path='',
    static_folder='./build',
    template_folder='./build'
)

CORS(app, resources={r"/api/*": {"origins": "*"}})
search_types_as_dict = { "vector": 1.0, "hybrid": 0.5, "text": 0 }

@app.route("/ping")
def index():
    return "pong!"


@app.route('/')
def index_redir():
    return render_template('index.html')


@app.route("/api/search", methods=["POST"])
def search():
    input = request.get_json()
    search_input = input["searchInput"]
    alpha = get_alpha_value(input["searchType"])
    search_input_vectorized = huggingFace_service.create_embeddings_from_search_input(search_input)
    weaviate_data = weaviate_service.search_weaviate(search_input, search_input_vectorized, alpha)
    return jsonify(weaviate_data)


def get_alpha_value(search_type): 
    return search_types_as_dict[search_type]
