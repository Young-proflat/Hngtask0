# Hngtask0
# Deploying a web Api

**Using Flask**
Flask is a lightweight and flexible web framework for Python, designed to build web applications and APIs with minimal setup. It provides built-in support for routing, request handling, and extensions like Flask-RESTful for API development. With its simplicity and scalability, Flask is ideal for creating RESTful APIs that can integrate with databases, authentication systems, and third-party services.

**Installation**
To install Flask, ensure you have Python installed, then run:

# pip install flask
If your project requires additional dependencies, install them using:
# pip install -r requirements.txt

# Deploying on Render
**Create a requirements.txt file**
Run the following command to generate a requirements.txt file containing all dependencies
# **pip freeze > requirements.txt** 
which render runs a gunicorn on your requirements.txt file 
# gunicorn: app:app


To Learn more check out this link below 
https://hng.tech/hire/python-developers
