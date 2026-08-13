from flask import Flask, jsonify
import os
import redis

app = Flask(__name__)

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))

redis_client = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    decode_responses=True
)


@app.route("/")
def home():
    try:
        redis_client.ping()

        return jsonify({
            "application": "Kubernetes CI/CD Reliability Demo",
            "status": "healthy",
            "redis": "connected"
        })

    except Exception as e:
        return jsonify({
            "application": "Kubernetes CI/CD Reliability Demo",
            "status": "unhealthy",
            "redis": "disconnected",
            "error": str(e)
        }), 503


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/ready")
def ready():
    try:
        redis_client.ping()

        return jsonify({
            "status": "ready",
            "redis": "connected"
        })

    except Exception:
        return jsonify({
            "status": "not ready"
        }), 503


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )