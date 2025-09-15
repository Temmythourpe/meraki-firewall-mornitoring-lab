from flask import Flask, request, jsonify
import datetime
import json
import os

app = Flask(__name__)

LOG_FILE = "webhook_events.log"

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.get_json(force=True)
        timestamp = datetime.datetime.now().isoformat()
        with open(LOG_FILE, "a") as f:
            f.write(f"[{timestamp}] {json.dumps(data)}\n")
        print(f" Webhook received: {data}")
        return jsonify({"status": "ok"}), 200
    except Exception as e:
        print(f" Error: {e}")
        return jsonify({"status": "error", "message": str(e)}), 400

@app.route("/", methods=["GET"])
def index():
    return "Meraki Webhook Receiver is running!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
