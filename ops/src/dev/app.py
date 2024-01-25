from flask import Flask, make_response

app = Flask(__name__)

@app.route('/')
def hello_world():
    # HTML content with a specific text color
    html_content = '<p style="color: blue;">Hello, World! from development team softility</p>'
    
    response = make_response(html_content)
    
    # Adding minimum required headers
    response.headers['Content-Type'] = 'text/html; charset=utf-8'
    response.headers['Server'] = 'Flask'
    
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090)
