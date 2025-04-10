# Inventory Project
Our Inventory Project for CIS4004

## Installation
1. Start a venv with python -m venv .venv
1. Activate the venv with .venv\Scripts\activate
1. Enter the directory with cd inventory_project
1. Install requirements with pip install -r requirements.txt
1. This project requires a OAuth Client ID, which for grading purposes is included but will be shut off afterwards.
1. Run migrations with python manage.py migrate
1. Run the server with python manage.py runserver
1. Open the server at http://localhost:8000/, 127.0.0.1 will not work due to API token requirements.

## AI
We used a variety of AI models, ChatGPT, Deepseek, and Github Copilot. Generally every file that we touched in the project was affected in one way or another, because our main two types of prompts were either asking how to do something or pasting an error and asking how to fix it. There were other miscellaneous prompts like organizing files or getting help with CSS.