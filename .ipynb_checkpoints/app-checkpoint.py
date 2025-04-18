###
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Witaj w moim API!'

@app.route('/mojastrona')
def mojastrona():
    return 'To jest moja strona!'

@app.route('/hello')
def hello():
    name = request.args.get('name')
    if name:
        return f"Hello {name}!"
    else:
        return "Hello!"

@app.route('/api/v1.0/predict')
def predict():
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))

        suma = num1 + num2
        prediction = 1 if suma > 5.8 else 0

        return {
            "prediction": prediction,
            "features": {
                "num1": num1,
                "num2": num2
            }
        }
    except (TypeError, ValueError):
        return {"error": "Podaj poprawne liczby jako num1 i num2, np. /predict?num1=2&num2=3"}


@app.route('/api')
def decision():
    try:
        x = float(request.args.get('x'))
        y = float(request.args.get('y'))

        if x > y:
            result = "x jest większe niż y"
        elif x < y:
            result = "x jest mniejsze niż y"
        else:
            result = "x jest równe y"

        return {'wynik': result}
    
    except (TypeError, ValueError):
        return {'error': 'Podaj poprawne liczby jako x i y w URL, np. /api?x=5&y=3'}

if __name__ == '__main__':
    app.run(debug=True)

###