from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/users')
def index():
    return jsonify({'users': ['bart simpson']})

if __name__ == '__main__':
    app.run(debug=True)
