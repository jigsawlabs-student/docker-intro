from flask import Flask, jsonify
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)

@app.route('/users')
def index():
    return jsonify({'users': ['bart simpson', 'lisa simpson']})

if __name__ == '__main__':
    app.run(debug=True)
