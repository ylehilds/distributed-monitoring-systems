# Distributed Monitoring Systems

A modular framework for **monitoring distributed infrastructure and services**.  
This repo includes collectors, scrapers, utilities, and storage backend using CockroachDB to help track availability, logins, and other system events at scale. It is designed with flexibility in mind, so different data sources and storage layers can be swapped in easily.

---

## ✨ Features

- **Monitoring Utilities**
    - `check_ssh.py` — checks SSH service availability on a given host.
    - `monitor_logins.py` — tracks user login activity for auditing/security.

- **Scraper Framework**
    - `scraper/` contains modular scrapers for collecting system/service metrics.

- **Monitoring Framework**
    - `monitoring/` holds reusable monitoring logic, abstractions, and orchestrators.

- **Storage Backend**
    - `cockroachdb/` for CockroachDB adapters.

- **Data Science Utilities**
    - `data_science/` includes experimental/analysis scripts for collected metrics.

- **Misc & Utils**
    - `util/` for helper functions.
    - `misc/` for supporting scripts and notes.

---

## 🛠 Tech Stack

- **Language:** Python 3.x
- **Databases:**
    - **CockroachDB** (distributed SQL database)
- **Utilities & Libraries:**
    - [paramiko](http://www.paramiko.org/) — SSH2 protocol library for Python (used in `check_ssh.py` and related monitoring scripts)
    - `sqlalchemy`
    - `psycopg2`
---

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- Access to CockroachDB
- `pip` or `pipenv` for dependency management

### Clone & Install
```bash
git clone https://github.com/ylehilds/distributed-monitoring-systems.git
cd distributed-monitoring-systems/monitoring
pip install -r requirements.txt
