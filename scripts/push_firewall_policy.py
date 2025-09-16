#!/usr/bin/env python3
"""
Push firewall rules (L3 + L7) from policy.yaml into a Meraki network.
Requires: pip install meraki pyyaml
"""

import meraki
import yaml
import os
import sys
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# ----------------------------
# Load config
# ----------------------------
API_KEY = os.getenv("MERAKI_API_KEY")  # store securely: export MERAKI_API_KEY="yourkey"
NETWORK_ID = os.getenv("MERAKI_NETWORK_ID")  # set to your target network ID

if not API_KEY or not NETWORK_ID:
    print("Please set MERAKI_API_KEY and MERAKI_NETWORK_ID environment variables.")
    sys.exit(1)

# ----------------------------
# Load policy.yaml
# ----------------------------
with open("policy.yaml", "r") as f:
    policy = yaml.safe_load(f)

l3_rules = policy.get("l3_rules", [])
l7_rules = policy.get("l7_rules", [])

# DEBUG PRINTS
print("DEBUG: Loaded L3 rules:", l3_rules)
print("DEBUG: Loaded L7 rules:", l7_rules)

# ----------------------------
# Meraki Dashboard API client
# ----------------------------
dashboard = meraki.DashboardAPI(API_KEY, suppress_logging=True)

# ----------------------------
# Push L3 rules
# ----------------------------
def push_l3():
    print("Updating L3 firewall rules...")
    try:
        response = dashboard.appliance.updateNetworkApplianceFirewallL3FirewallRules(
            NETWORK_ID,
            rules=l3_rules
        )
        print(" L3 rules updated successfully:", response)
    except meraki.APIError as e:
        print(f" L3 update failed: {e.status} {e.reason}")
        print(f"   Details: {e.message}")
    except Exception as e:
        print(f" Unexpected error (L3): {e}")


# ----------------------------
# Push L7 rules
# ----------------------------
def push_l7():
    print("Updating L7 firewall rules...")
    try:
        response = dashboard.appliance.updateNetworkApplianceFirewallL7FirewallRules(
            NETWORK_ID,
            rules=l7_rules
        )
        print(" L7 rules updated successfully:", response)
    except meraki.APIError as e:
        print(f" L7 update failed: {e.status} {e.reason}")
        print(f"   Details: {e.message}")
    except Exception as e:
        print(f" Unexpected error (L7): {e}")
