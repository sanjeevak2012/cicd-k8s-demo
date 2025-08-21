from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics


app = Flask(__name__)
metrics = PrometheusMetrics(app) # exposes /metrics


@app.get("/")
def home():
return jsonify({"message": "Hello from CI/CD on Kubernetes!"})


@app.get("/healthz")
def health():
return "ok", 200


if __name__ == "__main__":
app.run(host="0.0.0.0", port=8000)