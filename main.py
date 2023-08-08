from flask import Flask, request, jsonify

app = Flask(__name__)

def calc_fibonacci(n):
    if n < 0:
        raise ValueError("El valor debe ser un número NO negativo.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

@app.route('/api/fibonacci/<int:n>', methods=['GET'])
def get_fibonacci_value(n):
    try:
        fibonacci_value = calc_fibonacci(n)
        return jsonify({"value": fibonacci_value})
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400

if __name__ == '__main__':
    app.run(debug=True)
