# Collaborative Flask Application — Personal Library

A collaborative Flask app that lets users add books, give ratings , and write short reviews.  t.
---

## How to Build and Run with Docker Compose
### Clone the Repository
git clone https://github.com/<your-username>/flask-lab-project.git
cd flask-lab-project
### Open flask app in terminal 
in terminal: docker compose up 
Access the flask app through local browser.

| Member | Role | Responsibilities |
|---------|------|------------------|
| **Zainab (Backend Lead)** | Flask logic & API routes | Implements `app.py`, `/add`, `/health`, and `/books` routes; writes unit tests in `tests/test_app.py`. |
| **Mifrah + Zainab (Frontend & API Integration)** | Templates & static files | Builds `home.html` and `style.css`, connects frontend with Flask routes using Fetch API. |
| **Mifrah (DevOps Engineer)** | CI/CD & Docker setup | Creates `Dockerfile`, configures GitHub Actions workflow (`ci-cd.yml`), and tests builds on push to `main`. |
