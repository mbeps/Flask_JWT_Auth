This is a simple backend system built with Flask that allows users to sign up and log in using JWT-based REST API.
This is only for learning authentication using JWT and it should not be used in production. 

# **Requirements**
These are the requirements needed to run the project:
- Python 3.10+
- Poetry

# **Features**

- **Log In:** Users can log in to their account.
- **JWT Authentication:** Users can authenticate their requests with JWT.

# **Stack**

This project uses the following technologies:

- [Python](https://www.python.org/): Python is a powerful, easy-to-learn, and widely-used programming language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming.
- [Flask](https://flask.palletsprojects.com/): Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries.
- [JWT](https://jwt.io/): JSON Web Token (JWT) is an open standard (RFC 7519) that defines a compact and self-contained way for securely transmitting information between parties as a JSON object. 

# **Installation Instructions**

To run the project locally, you need to follow the below instructions:

## 1. **Clone the Project**
```sh
git clone https://github.com/username/Flask_JWT_Auth.git
```


## 2. **Install Dependencies**

Install dependencies using [Poetry](https://python-poetry.org/), a Python dependency management tool. If you don't have Poetry, you can install it following the [official guide](https://python-poetry.org/docs/#installation).

Navigate to the project directory and install dependencies:

```bash
cd Flask_JWT_Auth
poetry install
```

## 3. **Run Project** 
After installing dependencies, start the development server:

```bash
poetry run python app.py
```

The server should start at http://127.0.0.1:5000.

You can now use the API endpoints to log in and make authenticated requests.

**Note:** This project uses environment variables to keep sensitive information like your secret key. Please make sure to create a `.env` file in your root directory and define `SECRET_KEY` variable.

The login endpoint expects a 'username' and 'password' in the POST request. In this simple project, 'username' can be any string and the 'password' is '123456'. In a real-world application, these would typically be validated against a database.

**Note:** This is a basic example of JWT authentication. In a real-world application, user credentials would typically be verified against a database and passwords would not be hardcoded in the backend. Passwords should always be hashed and stored securely.