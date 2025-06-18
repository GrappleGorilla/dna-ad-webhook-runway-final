from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "DNA Ad Webhook is running."

@app.route("/deploy", methods=["POST"])
def deploy_ad_video():
    try:
        data = request.json
        print("Received ad campaign:", data)

        # Placeholder Runway API call simulation
        response = {"output": {"url": "https://example.com/fake-video.mp4"}}
        return jsonify(response)

    except Exception as e:
        print("Error:", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
