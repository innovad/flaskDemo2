from flask import Flask, render_template, request, session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'abc'

@app.route('/')
def form():
    if not 'products' in session:
        session['products'] = []
    return render_template('index.html', products=session['products'])


@app.route('/', methods=['POST'])
def data():
    session['products'].append(request.form['product'])
    session.modified = True
    return render_template('index.html', products=session['products'])


if __name__ == '__main__':
    app.run()
