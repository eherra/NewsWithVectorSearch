from app import app
from waitress import serve
from dotenv import load_dotenv
from os import getenv

load_dotenv()

if __name__ == "__main__":
    port = int(getenv('PORT', 5000))
    serve(app,port=port,host="0.0.0.0")
