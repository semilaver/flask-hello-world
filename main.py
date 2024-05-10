from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000) 

@app.route('/')
def hello():
    return 'Hello world with Flask'
