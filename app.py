from flask import Flask, render_template, request
from flask_session import Session

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
Session['products'] = []

@app.route('/')
def form():
    return render_template('index.html', products=Session['products'])


@app.route('/', methods=['POST'])
def data():
    Session['products'].append(request.form['product'])
    return render_template('index.html', products=Session['products'])


if __name__ == '__main__':
    app.run()
