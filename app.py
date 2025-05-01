from flask import Flask, send_from_directory, jsonify
from flask_cors import CORS
import os
import json

app = Flask(__name__, static_folder='.')
CORS(app)  # Erlaubt CORS-Zugriff fürs Frontend

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/signale.json')
def aktien_signale():
    try:
        with open('signale.json', encoding='utf-8') as f:
            daten = json.load(f)
        return jsonify(daten)
    except Exception as e:
        return jsonify({'fehler': str(e)}), 500

@app.route('/signale_forex.json')
def forex_signale():
    try:
        with open('signale_forex.json', encoding='utf-8') as f:
            daten = json.load(f)
        return jsonify(daten)
    except Exception as e:
        return jsonify({'fehler': str(e)}), 500

@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory('.', filename)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)