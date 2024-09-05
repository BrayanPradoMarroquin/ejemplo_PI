from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Hola Mundo, esto es un mensaje de prueba'})

@app.route('/Asistencia', methods=['POST'])
def asistencia():
    data = request.get_json()
    print(data)
    return jsonify({'message': 'Asistencia registrada'})

if __name__ == '__main__':
    app.run(debug=True)