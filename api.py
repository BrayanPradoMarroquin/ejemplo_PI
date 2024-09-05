from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

asistencia = []

@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Hola Mundo, esto es un mensaje de prueba'})

@app.route('/Asistencia', methods=['POST'])
def asistencia():
    data = request.get_json()
    asistencia.append(data)
    return jsonify({'message': 'Asistencia registrada'})

@app.route('/Asistencia', methods=['GET'])
def get_asistencia():
    return jsonify(asistencia)

if __name__ == '__main__':
    app.run(debug=True)