# News Search with vectors
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/kubernetes-%23326ce5.svg?style=for-the-badge&logo=kubernetes&logoColor=white)
![Azure](https://img.shields.io/badge/azure-%230072C6.svg?style=for-the-badge&logo=microsoftazure&logoColor=white)

>  Introduction to Data Science mini-project

## What

PoC application to show vector/hybrid search approaches for semantic information retrieval/relevance engineering purposes. 

The PoC includes data pipeline which fetches news articles from API, processes the data (e.g. vectorizing) and then storing the articles to vector database (Weaviate).

We have created an simple UI to try out the searches with any text input. You can find the app hosted here: \
<a>link to the app</a>

## Why Vectors?

With vectors you can have [lightning-fast querying](https://weaviate.io/blog/why-is-vector-search-so-fast), and with help of [cosine similarity](https://en.wikipedia.org/wiki/Cosine_similarity) - semantic searches are possible.

> "Vectors are numeric representations of data that capture certain features of the data. For example, in the case of text data, “cat” and “kitty” have similar meaning, even though the words “cat” and “kitty” are very different if compared letter by letter. For semantic search to work effectively, representations of “cat” and “kitty” must sufficiently capture their semantic similarity. This is where vector representations are used, and why their derivation is so important." [Vector Embeddings Explained](https://weaviate.io/blog/vector-embeddings-explained#what-exactly-are-vector-embeddings)

Example of the vectors: \
<code>
cat = [1.5, -0.4, 7.2, 19.6, 3.1, ..., 20.2] \
kitty = [1.5, -0.4, 7.2, 19.5, 3.2, ..., 20.8]
</code>

<img src="https://github.com/eherra/NewsWithVectorSearch/blob/main/docs/howVectorsWork.png" width="80%" heigth="80%">

<sup>photo credit: [kdnuggets](https://www.kdnuggets.com/2023/06/vector-databases-important-llms.html)</sup>

<img  />

## Tech stack

- Backend: 
    - Python
- Data pipeline:
    - Python (Pandas, NLTK)
- Frontend:
    - React
- Vector database:
    - [Weaviate](https://weaviate.io/)
- Embeddings (vectors) are created with <code>HuggingFace</code> hosted model <code>[sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)</code>

## How to run

Fill <code>.envs</code> in backend folder. See the [.env.example](https://github.com/eherra/NewsWithVectorSearch/blob/main/backend/.env.example)

Go to root folder and run:

```
docker build -t news-vector-search .
```

and then:

```
docker run -dp 5000:5000 -e PORT=5000 news-vector-search
```

The app is running on: http://localhost:5000/