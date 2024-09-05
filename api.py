from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

asistencias = []

@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Hola Mundo, esto es un mensaje de prueba'})

@app.route('/Asistencia', methods=['POST'])
def asistencia():
    data = request.get_json()
    asistencias.append(data)
    return jsonify({'message': 'Asistencia registrada'})

@app.route('/Asistencia', methods=['GET'])
def get_asistencia():
    return jsonify(asistencias)

if __name__ == '__main__':
    app.run(debug=True, port=4000, host='0.0.0.0')