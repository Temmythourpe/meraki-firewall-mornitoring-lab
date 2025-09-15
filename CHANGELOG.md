# Changelog
All notable changes to this project will be documented in this file.  
This project follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) style.  
Versioning will use **YYYY.MM.DD** tags for lab milestones.

---

## [2025.09.15] - Initial Setup
### Added
- Created project repo structure (`/docs`, `/scripts`, `/postman`, `/webhook_receiver`).
- Added `README.md` (skeleton project overview).
- Drafted `policy.yaml` with L3/L7 firewall rules & content filtering.
- Added Flask webhook receiver (`webhook_receiver/app.py`).
- Added Python script `push_firewall_policy.py` for policy-as-code.
- Added Python script `list_assets.py` for org/network/device discovery.
- Added Python script `export_events.py` for exporting security events (JSON & CSV).

---

## [Unreleased]
### Planned
- Example Postman collection (`/postman/`) with key API calls.
- Syslog integration with SIEM (e.g., Wazuh).
- GitHub Actions workflow to run policy compliance check.
- Additional documentation in `/docs/`:
  - Firewall design notes
  - Monitoring workflows
  - API automation guide

