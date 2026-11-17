import os

from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

VERSION = os.getenv('APP_VERSION', '1.0.0')


@app.route('/')
def home():
    return '<h1>Welcome to homelab-app</h1>'


@app.route('/health')
def health():
    return jsonify({'status': 'ok', 'version': VERSION}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
