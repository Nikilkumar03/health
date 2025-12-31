# Port Demo App

## What this app does
A simple Flask application exposing `/` and `/health`, containerized using Docker and orchestrated with Docker Compose.

---

## Ports Explained

- The application listens on port **5000** (defined by APP_PORT).
- The container exposes port **5000**.
- Docker Compose maps host port **8080 → 5000**.

This allows external users to access the app without changing the container’s internal configuration.

---

## Traffic Flow

User → localhost:8080 → Docker → Container:5000 → Flask App

---

## Running the App

```bash
docker compose up --build
