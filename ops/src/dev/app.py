from flask import Flask, render_template

app = Flask(__name__)

# Health check endpoint
@app.route('/health')
def health_check():
    return 'OK', 200

# Your main endpoint
@app.route('/')
def hello_world():
    try:
        return render_template('index.html')
    except Exception as e:
        app.logger.error(f"An error occurred: {e}")
        return "Internal Server Error", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090)
