from fetching import fetcher
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return fetcher.get_random_player()