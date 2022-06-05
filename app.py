from flask import Flask, render_template, request

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

products = []

@app.route('/')
def form():
    return render_template('index.html', products=products)


@app.route('/', methods=['POST'])
def data():
    products.append(request.form['product'])
    return render_template('index.html', products=products)


if __name__ == '__main__':
    app.run()
