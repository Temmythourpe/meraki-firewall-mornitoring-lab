from flask import Flask, request, jsonify, render_template_string
import datetime
import json
import os

app = Flask(__name__)

LOG_FILE = "webhook_events.log"

# -----------------------------
# Webhook receiver
# -----------------------------
@app.route("/meraki/webhook", methods=["POST"])
def meraki_webhook():
    try:
        data = request.get_json(force=True)
        timestamp = datetime.datetime.now().isoformat()
        with open(LOG_FILE, "a") as f:
            f.write(f"[{timestamp}] {json.dumps(data)}\n")
        print(f"Webhook received: {data}")
        return jsonify({"status": "ok"}), 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"status": "error", "message": str(e)}), 400

# -----------------------------
# Dashboard view
# -----------------------------
@app.route("/dashboard", methods=["GET"])
def dashboard():
    events = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            for line in f:
                try:
                    timestamp, event_json = line.strip().split(" ", 1)
                    event = json.loads(event_json)
                    events.append({"timestamp": timestamp, **event})
                except Exception:
                    continue

    html = """
    <html>
    <head><title>Meraki Webhook Dashboard</title></head>
    <body>
        <h2>Webhook Events</h2>
        <table border="1" cellpadding="5" cellspacing="0">
            <tr><th>Timestamp</th><th>Event Type</th><th>Message</th></tr>
            {% for e in events %}
            <tr>
                <td>{{ e.timestamp }}</td>
                <td>{{ e.eventType if e.eventType else 'N/A' }}</td>
                <td>{{ e.message if e.message else e }}</td>
            </tr>
            {% endfor %}
        </table>
    </body>
    </html>
    """
    return render_template_string(html, events=events)

# -----------------------------
# Root endpoint
# -----------------------------
@app.route("/", methods=["GET"])
def index():
    return "Meraki Webhook Receiver is running! Access /dashboard to see events."

# -----------------------------
# Main
# -----------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="127.0.0.1", port=port, debug=True)
