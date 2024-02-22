from flask import Flask

app = Flask(__name__)

@app.route('/calc/add/<int:num1>/<int:num2>')
def add(num1, num2):
    result = num1 + num2
    return f'{result}'

@app.route('/calc/sub/<int:num1>/<int:num2>')
def subtract(num1, num2):
    result = num1 - num2
    return f'{result}'

@app.route('/calc/mul/<int:num1>/<int:num2>')
def multiply(num1, num2):
    result = num1 * num2
    return f'{result}'

@app.route('/calc/div/<int:num1>/<int:num2>')
def divide(num1, num2):
    if num2 == 0:
        return 'Error: Division by zero!'
    result = num1 / num2
    return f'{result}'

if __name__ == '__main__':
    app.run()