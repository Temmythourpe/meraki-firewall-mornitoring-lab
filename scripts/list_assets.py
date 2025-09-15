#!/usr/bin/env python3
"""
List Meraki organizations, networks, and devices.
Requires: pip install meraki
"""

import meraki
import os
import sys

# ----------------------------
# Load API key
# ----------------------------
API_KEY = os.getenv("MERAKI_API_KEY")

if not API_KEY:
    print(" Please set MERAKI_API_KEY as an environment variable.")
    print("   Example: export MERAKI_API_KEY='your_api_key_here'")
    sys.exit(1)

# ----------------------------
# Initialize Meraki Dashboard API client
# ----------------------------
dashboard = meraki.DashboardAPI(API_KEY, suppress_logging=True)

# ----------------------------
# List organizations
# ----------------------------
print("\n Fetching organizations...")
orgs = dashboard.organizations.getOrganizations()

for org in orgs:
    print(f"\n Org: {org['name']} (ID: {org['id']})")

    # ----------------------------
    # List networks per org
    # ----------------------------
    nets = dashboard.organizations.getOrganizationNetworks(org['id'])
    for net in nets:
        print(f" Network: {net['name']} (ID: {net['id']})")
        
        # ----------------------------
        # List devices per network
        # ----------------------------
        devices = dashboard.networks.getNetworkDevices(net['id'])
        for dev in devices:
            print(f" Device: {dev['model']} | Serial: {dev['serial']} | MAC: {dev['mac']}")
