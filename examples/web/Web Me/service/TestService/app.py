from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "CyberBlitz2025{flag}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
