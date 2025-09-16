# Firewall Policy Documentation

This document describes the Layer 3 (L3) and Layer 7 (L7) firewall rules applied in this Cisco Meraki project.  
The policy is defined as **Infrastructure-as-Code (IaC)** in [`policy.yaml`](../policy.yaml), which can be applied via the Meraki Dashboard API.

---

## Layer 3 Firewall Rules (L3)

These rules control **traffic between IP subnets**.

| Rule # | Action  | Protocol | Source        | Destination   | Port(s) | Description                  |
|--------|---------|----------|---------------|---------------|---------|------------------------------|
| 1      | allow   | tcp      | 10.0.0.0/24   | 192.168.1.0/24 | 443     | Allow HTTPS traffic from LAN to DMZ |
| 2      | allow   | udp      | 10.0.0.0/24   | any           | 53      | Allow DNS queries from LAN to external servers |
| 3      | deny    | any      | any           | 10.0.99.0/24  | any     | Block guest network from reaching internal servers |
| 4      | deny    | any      | any           | any           | any     | Implicit deny (default) |

**Best Practice**: Explicitly block guest/Wi-Fi subnets from sensitive VLANs.  
**Monitoring**: Use API queries (`getL3FirewallRules`) to validate applied rules.  

---

## Layer 7 Firewall Rules (L7)

These rules control **traffic based on application categories and URLs**.

| Rule # | Action | Category / App | Example Matches |
|--------|--------|----------------|-----------------|
| 1      | deny   | `socialMedia`  | Facebook, Instagram, TikTok |
| 2      | deny   | `adultContent` | Pornography, gambling sites |
| 3      | allow  | `collaboration` | Microsoft Teams, Zoom, Google Meet |
| 4      | allow  | `productivity` | Office 365, Slack, GitHub |

**Best Practice**: Block **non-business categories** while explicitly allowing collaboration/productivity tools.  
**Monitoring**: Use the **Meraki Security Events API** to confirm if L7 blocks are triggering.  

---

## Content Filtering Policy

The following **content categories** are blocked at the MX:

- Adult & Explicit Content  
- Gambling  
- Malware Sites  
- Social Media (work hours only – can be scheduled in Dashboard)

---

## Logging & Monitoring

- **Webhook Receiver**: Events (e.g., firewall blocks) are forwarded to a local Flask app (`webhook_receiver/app.py`).  
- **Syslog Export**: Can be integrated into Wazuh/SIEM.  
- **Postman Collection**: `Meraki_Firewall_Monitoring.postman_collection.json` allows pulling firewall rules & event logs via API.

---

## Future Enhancements

- Role-based firewall rules (per VLAN)  
- Time-based policies (e.g., block social media during work hours)  
- Integration with GitHub Actions → automatically check if current rules match `policy.yaml`  

---

**References**
- [Meraki Dashboard API Docs](https://developer.cisco.com/meraki/api-v1/)  
- [Firewall Rules Guide](https://documentation.meraki.com/MX/Firewall_and_Traffic_Shaping)  
