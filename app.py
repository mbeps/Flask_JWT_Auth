from flask import Flask, request, jsonify, make_response, request, render_template, session, flash
import jwt
from datetime import datetime, timedelta
from functools import wraps
from environ import Env

# set up environment
env = Env()
env.read_env()

app: Flask = Flask(__name__)

# Get the secret key
app.config['SECRET_KEY'] = env('SECRET_KEY')


def token_required(func):
    """
    A decorator function for verifying the JWT

    Args:
        func (function): The function to decorate

    Returns:
        function: Decorated function
    """
    @wraps(func)
    def decorated(*args, **kwargs):
        # get the token from request arguments
        token = request.args.get('token') 
        
        # if no token is provided, return an error
        if not token:
            return jsonify({'Alert!': 'Token is missing!'}), 401

        try:
            # decode the token using the app's secret key
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'
        except:
            return jsonify({'Message': 'Invalid token'}), 403

        # call the decorated function
        return func(*args, **kwargs)
    return decorated


@app.route('/')
def home():
    """
    Home page view handler.

    Returns:
        str: HTML template or logged in message
    """
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return 'logged in currently'


@app.route('/public')
def public():
    """
    Public view handler.

    Returns:
        str: Message available for all
    """
    return 'For Public'


@app.route('/auth')
@token_required
def auth():
    """
    Authenticated view handler. Only accessible with a valid JWT.

    Returns:
        str: Welcome message
    """
    return 'JWT is verified. Welcome to your dashboard !  '


@app.route('/login', methods=['POST'])
def login():
    """
    Login view handler. 

    Returns:
        Union[Response, str]: JWT token for the user if valid credentials provided, else an error message.
    """
    if request.form['username'] and request.form['password'] == '123456':
        session['logged_in'] = True

        # encode a JWT with the username and an expiration time
        token = jwt.encode({
            'user': request.form['username'],
            'expiration': str(datetime.utcnow() + timedelta(seconds=60))
        },
            app.config['SECRET_KEY'])
        return jsonify({'token': token.decode('utf-8')})
    else:
        return make_response('Unable to verify', 403, {'WWW-Authenticate': 'Basic realm: "Authentication Failed "'})


@app.route('/logout', methods=['POST'])
def logout():
    """
    Logout view handler. Invalidates the user session.

    Returns:
        TBD: implementation needed
    """
    pass
# your code goes here


if __name__ == "__main__":
    app.run(debug=True)
