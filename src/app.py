from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello')
def hello():
    return render_template('hello.html')


@app.route('/summary')
def summary():
    return render_template('summary.html')


@app.route('/calc', methods=['GET', 'POST'])
def calc():
    if request.method == 'POST':
        result = int(request.form['x']) + int(request.form['y'])

        return render_template('calc.html', result=result)

    return render_template('calc.html', result=None)


if __name__ == '__main__':
    app.run(debug=True)
