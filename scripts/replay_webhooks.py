import json
import requests
import os

# Load sample webhook events
SAMPLE_FILE = os.path.join(os.path.dirname(__file__), "../sample_data/sample_webhooks.json")

with open(SAMPLE_FILE, "r") as f:
    events = json.load(f)

WEBHOOK_URL = "http://127.0.0.1:5000/meraki/webhook"  # local Flask server

for i, event in enumerate(events, start=1):
    try:
        response = requests.post(WEBHOOK_URL, json=event)
        if response.status_code == 200:
            print(f"[{i}] Event sent successfully: {event['eventType']}")
        else:
            print(f"[{i}] Failed to send event: {response.status_code} {response.text}")
    except Exception as e:
        print(f"[{i}] Exception sending event: {e}")
