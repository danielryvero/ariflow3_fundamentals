# 🚀 Airflow Certification Practice Project (Astro CLI)

This repository contains the DAGs and exercises I developed while preparing for the **Apache Airflow certification**, using the **Astro CLI** local development environment.

The goal of this project is simple:

> Clone → Start → Explore DAGs → Learn

The project runs locally using **Docker** and the **Astro CLI**, which packages Apache Airflow into reproducible containers.

---

# 🧰 Prerequisites

This setup assumes **macOS** using **Homebrew**.

## 1️⃣ Install Docker Desktop

```bash
brew install --cask docker
```

Start Docker Desktop and ensure it is running.

Verify installation:
```bash
docker --version
docker compose version
```

## 2️⃣ Install Astro CLI
```bash
brew install astro
```

Verify installation:
```bash
astro version
```

Astro CLI allows you to run Apache Airflow locally inside Docker containers.

---

## 📥 Clone the Repository
```bash
https://github.com/danielryvero/ariflow3_fundamentals.git
cd local_airflow
```

# ▶️ Start Airflow Locally

From the root of the project:
```bash
astro dev start
```

This will:
* Build the Docker image
* Start the Airflow containers
* Initialize the metadata database
* Launch the webserver and scheduler

Once running, open:
```bash
http://localhost:8080
```
Default credentials:
```bash
Username: admin
Password: admin
```
## ⚠️ Common Issue: Port 5432 Already in Use
If you see an error similar to:
```bash
Ports are not available: exposing port TCP 127.0.0.1:5432
```

It likely means a local PostgreSQL service is already running (for example, from a previous Airflow or Postgres installation).

Check which process is listening on that port:
```bash
sudo lsof -nP -iTCP:5432 | grep LISTEN
```

If it's a local Postgres instance, stop it:
```bash
sudo pkill postgres
```

Then restart the environment:
```bash
astro dev start
```
Airflow should now start normally.

# 📂 DAG Structure

All DAGs are located inside the /dags directory:
```bash
dags/
├── backfill_trigger_dag.py   -> Basic DAG example
├── check_dag.py              -> Variation of a simple DAG structure
├── exampledag.py             -> Task definition examples
├── my_dag.py                 -> Example of sensor usage with decorators
├── my_dag2.py                -> Demonstrates inter-task communication using XCom
├── my_task.py                -> Backfill and trigger examples
├── print_variable.py         -> Validation and conditional checks
├── sensor_decorator.py       -> Demonstrates Airflow Variables usage
└── xcom_dag.py               -> General example DAG
```
🔄 Useful Astro Commands

Stop the environment:
```bash
astro dev stop
```
Restart services:
```bash
astro dev restart
```
Force rebuild containers:
```bash
astro dev start --force-rebuild
```
Destroy the environment completely:
```bash
astro dev kill
```
