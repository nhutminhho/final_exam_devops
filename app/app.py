from flask import Flask
# import mysql.connector
# import json

app = Flask(__name__)


@app.route('/')
def index():
  return "Welcome to Docker at CSC"

if __name__ == "__main__":
  app.debug=True
  app.run(host='0.0.0.0', port=5000)
