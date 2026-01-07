from flask import Flask, request, jsonify
from asteval import Interpreter

app = Flask(__name__)
aeval = Interpreter()

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    expression = data.get('expression')

    if not expression:
        return jsonify({'error': 'Invalid expression.'}), 400

    try:
        # Safely evaluate the expression
        result = aeval.eval(expression)
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': 'Invalid expression.'}), 400

if __name__ == '__main__':
    app.run(debug=True)