from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! form softility devops team anil,prasanna and Ajay'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090)
