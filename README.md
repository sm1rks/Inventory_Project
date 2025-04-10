# Inventory Project
Our Inventory Project for CIS4004

## Installation
1. Start a venv with python -m venv .venv
1. Activate the venv with .venv\Scripts\activate
1. Enter the directory with cd inventory_project
1. Install requirements with pip install -r requirements.txt
1. Run migrations with python manage.py migrate
1. Run the server with python manage.py runserver
1. Open the server at http://localhost:8000/, 127.0.0.1 will not work due to API token requirements.