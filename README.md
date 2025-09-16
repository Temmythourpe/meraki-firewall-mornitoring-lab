# Cisco Meraki Firewall & Monitoring Lab

## Project Overview
This project demonstrates how to configure and monitor enterprise firewalls using the **Cisco Meraki Dashboard**.  
The lab was built with the **Meraki DevNet Sandbox** and **Dashboard API**, without requiring physical hardware.  

The goal is to show:
- Firewall configuration (L3/L7 rules, content filtering, geo-blocking).
- System monitoring (alerts, webhooks, syslog).
- Automation via **Postman** and **Python SDK**.
- Policy-as-code approach (YAML → API push).

---

## Tools & Setup
- Cisco Meraki DevNet Sandbox / Demo Dashboard  
- Meraki Dashboard API + API Key  
- Postman (Meraki collections)  
- Python 3.x + meraki SDK (pip install meraki)  
- Flask (for webhook receiver)  
- GitHub for version control & documentation  

---

## Firewall Policy
- **Layer 3 (L3)**: Deny RFC1918 outbound, block risky ports, allow HTTP/HTTPS.  
- **Layer 7 (L7)**: Block P2P, gaming, malware domains, and specific categories.  
- **Content Filtering**: Talos security categories enabled.  

See [`policy.yaml`](./policy.yaml) for rules-as-code.  

---

## Monitoring
- **Webhooks**: Alerts sent to a custom Flask receiver.  
- **Syslog**: Security events forwarded to SIEM (optional: Wazuh).  
- **Dashboard**: Client/device analytics, event logs, usage trends.  

---

## Automation
- **Postman**: Test APIs (list orgs, networks, firewall rules).  
- **Python**:
  - `scripts/list_assets.py` → enumerate orgs/networks/devices.  
  - `scripts/push_firewall_policy.py` → apply rules from YAML.  
  - `scripts/export_events.py` → save security events to JSON/CSV.  

## Limitations

This lab was built using the Cisco Meraki DevNet **Always-On Sandbox**.  
The sandbox allows API authentication and network queries, but write operations (such as updating firewall policies) return `403 Forbidden` because it only gives read-only for firwall updates.  

This is expected behavior for the Always-On environment.  
In a real Meraki environment (or in a Reserved Sandbox), the same automation would successfully apply the firewall rules.

- Sandbox API is temporary
- Webhook receiver uses sample events
- Real webhooks will only work while the sandbox exists.
- Scripts demonstrate automation and policy-as-code workflow
- Offline replay demonstrates monitoring functionality without live Meraki resources.
Project Insights

This section provides a guide to the Postman workflow, API endpoints, and limitations encountered while building the lab.

API Endpoints Used

GET List Organizations – Retrieve all organizations accessible by your API key.

GET List Networks – Retrieve networks under a selected organization.

PUT Push L3 Firewall Rules – Apply Layer 3 firewall rules from policy.yaml.

PUT Push L7 Firewall Rules – Apply Layer 7 firewall rules from policy.yaml.

POST Send Sample Webhook Event – Send a test event to the local Flask webhook receiver.

Postman Workflow

Start with GET List Organizations to identify the target organization.

Use GET List Networks to retrieve the network ID for firewall configuration.

Apply PUT Push L3 Firewall Rules to enforce basic network-level access policies.

Apply PUT Push L7 Firewall Rules to enforce application-level access policies.

Test POST Send Sample Webhook Event to ensure the local Flask receiver correctly logs events.

Sandbox Limitations

The Meraki Always-On Sandbox is read-only for firewall and content filtering write operations.

L3/L7 firewall push requests return 403 Forbidden.

Content Filtering API returns 404 Page Not Found.

These responses are expected and are included in the project to demonstrate workflow automation and policy-as-code practices.

Webhook simulation is fully functional locally via the Flask receiver.

Visual References

Postman Screenshots – Show the request bodies, headers, and workflow order.

Webhook Logs – Demonstrate received events in webhook_events.log or console output.