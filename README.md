# Server Monitoring & Email Alert System

This project is a personal development project to practice FastAPI, MongoDB, and background tasks.  

The goal of the project is to monitor servers and send email alerts when a server does not respond or returns an unexpected response.  

---

## Features

- Periodically check servers via HTTP or ICMP (ping) requests.
- Detect server errors or unexpected responses and generate "critical/warning" status.
- Send email alerts only for the first failure and again after 1 hour if the problem continues.
- Monitored servers, alert recipients, and thresholds can be managed in the database.
- Server-specific settings:
  - Check interval (how often the server is checked)
  - Timeout duration for requests
  - Number of consecutive failures before sending an alert
  - Enable/disable server monitoring
- CRUD operations for servers:
  - `GET /servers` – List all monitored servers
  - `POST /servers` – Add a new server to monitor
  - `GET /servers/{id}` – Get details of a specific server
  - `PUT /servers/{id}` – Update server settings
  - `DELETE /servers/{id}` – Remove a server from monitoring
