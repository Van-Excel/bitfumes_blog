Blog API
A simple Blog API built using FastAPI. This project provides a basic CRUD (Create, Read, Update, Delete) interface for managing blog posts.

Table of Contents
Getting Started
Installation
Running the Application
API Documentation
Project Structure
Contributing
License
Getting Started
Follow the instructions below to set up and run the project locally.

Prerequisites
Make sure you have Python 3.7+ installed on your system. You can download it from here.

You will also need pip (Python's package installer) to install dependencies.

Installation
Clone the repository

bash
Copy code
git clone <https://github.com/Van-Excel/bitfumes_blog.git>
cd blog-api
Create and activate a virtual environment (optional, but recommended)

bash
Copy code
python3 -m venv env
source env/bin/activate  # On Windows: `env\Scripts\activate`
Install dependencies Install all required dependencies using pip:

bash
Copy code
pip install -r requirements.txt
Running the Application
Start the FastAPI server Run the following command to start the server:

bash
Copy code
python main.py
Access the API Once the server is running, you can access the local API documentation:

API Docs (Swagger UI): <http://localhost:8000/docs>
Alternative API Docs (ReDoc): <http://localhost:8000/redoc>
API Documentation
FastAPI automatically generates interactive API documentation using Swagger UI. You can access it by navigating to the /docs endpoint when the server is running.

Example Endpoints
GET /blogs/ - Retrieve a list of all blog posts
POST /blog/ - Create a new blog post
GET /blog/{id} - Retrieve a specific blog post by ID
PUT /blog/{id} - Update a specific blog post by ID
DELETE /blog/{id} - Delete a specific blog post by ID
