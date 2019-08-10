# PyWeb

Implementation of a very simple webserver in Python (using Python3.8 to figure out new syntax) to learn and understand how it works.

## How to use it?

- Install Python3.8 from deadsnakes ppa
- sudo add-apt-repository ppa:deadsnakes/ppa
- sudo apt-get update
- sudo apt-get install python3.8\*
- $ git clone https://github.com/ghostbill/pyweb.git
- $ cd pyweb/
- $ python3 -m venv venv
- $ source venv/bin/activate
- (venv) $ pip install --update pip
- (venv) $ pip install pyramid
- (venv) $ pip install flask
- (venv) $ pip install django
Start the server with:
- (venv) $ python3 demoserver.py # Initial barebones server
OR
- (venv) $ python3 wsgiapp.py flaskapp:app # Test the wsgi concept with a flask app
OR
- (venv) $ python3 wsgiapp.py pyramidapp:app # Test the wsgi concept with a pyramid app
OR
- (venv) $ python3 wsgiapp.py flaskapp:app # Test the wsgi concept with a flask
app

After trying one of the command to start/test the server go to your browser and type http://localhost:7777/hello or open a new terminal and type $ curl -v http://localhost:7777/hello

To test for concurrency:
- (venv) $ python3 wsgidemoserver\_con.py # To start the server

Try running multiple instances of http://localhost:7777/hello in your browser and curl -v http://localhost:7777/hello in your terminal and see how your server can handle multiple requests at the same time.
