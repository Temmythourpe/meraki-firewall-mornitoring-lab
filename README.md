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
The sandbox allows API authentication and network queries, but write operations (such as updating firewall policies) return `403 Forbidden` because it only gives read-only for firewall updates.  

This is expected behavior for the Always-On environment.  
In a real Meraki environment (or in a Reserved Sandbox), the same automation would successfully apply the firewall rules.

- Sandbox API is temporary
- Webhook receiver uses sample events
- Real webhooks will only work while the sandbox exists.
- Scripts demonstrate automation and policy-as-code workflow
- Offline replay demonstrates monitoring functionality without live Meraki resources.

*Postman Workflow*

The Postman collection demonstrates a realistic automation workflow:

Discover

GET List Organizations → verify available organizations.

GET List Networks → verify available networks.

Configure Firewall Rules

PUT Push L3 Firewall Rules → apply L3 rules from policy.yaml.

PUT Push L7 Firewall Rules → apply L7 rules from policy.yaml.

Monitor & Test Events

POST Send Sample Webhook Event → test the local Flask receiver (app.py).

Verify the events are logged locally in webhook_events.log.

Notes: Due to the Meraki Always-On Sandbox:

Firewall write operations return 403 Forbidden (L3 & L7).

Content Filtering API endpoints are unavailable (would return 404).

These limitations are expected and noted as part of the project.