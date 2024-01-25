from flask import Flask, make_response

app = Flask(__name__)

@app.route('/')
def hello_world():
    response = make_response('Hello, World! from development team softility')
    
    # Adding minimum required headers
    response.headers['Content-Type'] = 'text/plain; charset=utf-8'
    response.headers['Server'] = 'Flask'
    
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090)
