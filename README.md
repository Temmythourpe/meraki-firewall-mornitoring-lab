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

