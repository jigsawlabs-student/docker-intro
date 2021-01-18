from flask import Flask


app = Flask(__name__)

app.config.from_object('project.config.DevelopmentConfig')

@app.route('/users')
def index():
    return {'users': ['bart simpson']}

if __name__ == '__main__':
    app.run(debug=True)
