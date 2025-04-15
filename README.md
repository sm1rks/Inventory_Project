# Inventory Project
Our Inventory Project for CIS4004

## Installation
1. Start a venv with python -m venv .venv
1. Activate the venv with .venv\Scripts\activate
1. Enter the directory with cd inventory_project
1. Install requirements with pip install -r requirements.txt
1. This project requires a OAuth Client ID, see below for how to create one.
1. Run migrations with python manage.py migrate
1. Run the server with python manage.py runserver
1. Open the server at http://localhost:8000/, 127.0.0.1 will not work due to API token requirements.

## API
1. Visit the APIs & Services page at https://console.developers.google.com/apis
1. Click "Create project"
1. Name and create the project
1. Click Credentials > Create credentials > OAuth client ID
1. Click configure consent screen > Get started > Fill out the form, choose External Audience
1. Click Create OAuth client > Choose Web application for Application type
1. Add http://localhost and http://localhost:8000 as Authorized JavaScript origins
1. Add http://localhost:8000/login/auth-receiver/ as Authorized redirect URIs
1. Copy the Client ID and save it for later
1. Click Data Access and Add a scope
1. Add userinfo.email and openid as scopes
1. Click Audience and add your Google account as a Test user
1. Paste the Client ID into the example.env found in inventory_project/inventory_project
1. Rename example.env to .env

The ID previously attached to this repo has been disabled.

## AI
We used a variety of AI models, ChatGPT, Deepseek, and Github Copilot. Generally every file that we touched in the project was affected in one way or another, because our main two types of prompts were either asking how to do something or pasting an error and asking how to fix it. There were other miscellaneous prompts like organizing files or getting help with CSS.