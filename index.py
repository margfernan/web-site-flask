from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('gastos.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/gastos')
def gastos():
    return render_template('gastos.html')

@app.route('/gastos_listado')
def gastos_listado():
    return render_template('gastos_listado.html')


if __name__ == '__main__':
    app.run(debug=True)
