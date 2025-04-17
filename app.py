from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"message": "Welcome to Solana Pairs API!"})

@app.route('/solana-pairs')
def get_solana_pairs():
    url = "https://api.dexscreener.com/latest/dex/pairs/solana"
    response = requests.get(url)
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Failed to fetch data"}), response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
