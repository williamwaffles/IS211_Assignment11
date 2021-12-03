from flask import Flask, render_template, redirect, request
import re

app = Flask(__name__)

todo = []

@app.route('/')
def index():
    return render_template('index.html', todo=todo)

@app.route('/newtask', methods=['POST'])
def newtask():
    task = request.form['Task']
    priority = request.form['Priority']
    email = request.form['Email Address']

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return redirect('/')
    elif not task:
        return redirect('/')
    elif priority == 'Priority':
        return redirect('/')
    else:
        todo.append((task, priority, email))
    print(todo)
    return redirect('/')


@app.route('/clear', methods=['POST'])
def clear():
    del todo[:]
    return redirect('/')


if __name__ == '__main__':
    app.run()
