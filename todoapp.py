from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route('/main')
def main():

    return render_template('index.html')

@app.route('/')
def new():

    return redirect(url_for('main'))



@app.route('/hello/<name>')
def call_name(name):

    return f'Hi, {name}!'

'''@app.route('/adder/<x>/<y>')
def adder(x, y):
    sum = float(x) + float(y)
    return f'{x} + {y} = {sum}'
'''


if __name__ == '__main__':

    app.run(debug=True)