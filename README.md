# Blog API

A simple Blog API built using [FastAPI](https://fastapi.tiangolo.com/). This project provides a basic CRUD (Create, Read, Update, Delete) interface for managing blog posts.

## Table of Contents

- [Getting Started](#getting-started)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [API Documentation](#api-documentation)
- [Project Structure](#project-structure)

---

## Getting Started

Follow the instructions below to set up and run the project locally.

### Prerequisites

Make sure you have Python 3.7+ installed on your system. You can download it from [here](https://www.python.org/downloads/).

You will also need `pip` (Python's package installer) to install dependencies.

### Installation

1. **Clone the repository**

   ```bash

   git clone https://github.com/Van-Excel/bitfumes_blog.git
   cd bitfumes_blog

2. **Create and activate a virtual environment (optional, but recommended)**

   ```
   python3 -m venv env
   source env/bin/activate  # On Windows: `env\Scripts\activate`


3. **Install dependencies Install all required dependencies using pip:**

   ```
   pip install -r requirements.txt


# Running the Application

1. **Start the FastAPI server Run the following command to start the server:**

   ```
   python main.py


2. **Access the API Once the server is running, you can access the local API documentation:**

   ```
   API Docs (Swagger UI): <http://localhost:8000/docs>
   Alternative API Docs (ReDoc): <http://localhost:8000/redoc>
   API Documentation
   FastAPI automatically generates interactive API documentation using Swagger UI. You can access it by navigating to the /docs endpoint when the server is running.


# Project Structure

   ```
   ├── app
   │   ├── **init**.py
   │   ├── models.py        # Database models
   │   ├── schemas.py       # Pydantic models (validation)
   │   ├── main.py          # Main application file
   │   ├── routes.py        # API routes
   │   └── database.py      # Database connection setup
   ├── tests                # Unit and integration tests
   ├── requirements.txt     # List of dependencies
   ├── README.md            # Project documentation



# Example Endpoints
GET /blogs/ - Retrieve a list of all blog posts
POST /blog/ - Create a new blog post
GET /blog/{id} - Retrieve a specific blog post by ID
PUT /blog/{id} - Update a specific blog post by ID
DELETE /blog/{id} - Delete a specific blog post by ID
