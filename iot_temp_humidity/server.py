from flask import Flask, Response, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def startServer():
    app.run(host='0.0.0.0', threaded=True)