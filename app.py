from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hi Team - our first API on Heroku worked!!!!'

if __name__ == '__main__':
    app.run(debug=True)