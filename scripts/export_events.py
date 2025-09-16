#!/usr/bin/env python3
"""
Export Meraki security events to JSON and CSV.
Requires: pip install meraki pandas
"""

import meraki
import os
import sys
import json

from datetime import datetime, timedelta
from dotenv import load_dotenv 
# ----------------------------
# Load API key & network ID
# ----------------------------
API_KEY = os.getenv("MERAKI_API_KEY")
NETWORK_ID = os.getenv("MERAKI_NETWORK_ID")

if not API_KEY or not NETWORK_ID:
    print("Please set MERAKI_API_KEY and MERAKI_NETWORK_ID environment variables.")
    sys.exit(1)

# ----------------------------
# Initialize Meraki Dashboard API client
# ----------------------------
dashboard = meraki.DashboardAPI(API_KEY, suppress_logging=True)

# ----------------------------
# Time window (last 24 hours)
# ----------------------------
end_time = datetime.utcnow()
start_time = end_time - timedelta(days=1)

iso_start = start_time.isoformat() + "Z"
iso_end = end_time.isoformat() + "Z"

print(f" Fetching events from {iso_start} to {iso_end}")

# ----------------------------
# Fetch security events
# ----------------------------
try:
    events = dashboard.networks.getNetworkEvents(
        NETWORK_ID,
        productType="appliance",   # Focus on MX security events
        perPage=1000,
        t0=iso_start,
        t1=iso_end
    )
except Exception as e:
    print(f" Error fetching events: {e}")
    sys.exit(1)

# ----------------------------
# Save to JSON
# ----------------------------
timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
json_file = f"security_events_{timestamp}.json"

with open(json_file, "w") as f:
    json.dump(events, f, indent=2)

print(f" Saved {len(events.get('events', []))} events to {json_file}")

# ----------------------------
# Save to CSV
# ----------------------------
if "events" in events:
    df = pd.DataFrame(events["events"])
    csv_file = f"security_events_{timestamp}.csv"
    df.to_csv(csv_file, index=False)
    print(f" Saved events to {csv_file}")
else:
    print("No events found in this time range.")
