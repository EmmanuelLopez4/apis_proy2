
from flask import Flask, request, jsonify
import cv2
import os

app = Flask(__name__)

DATASET = "dataset"
os.makedirs(DATASET, exist_ok=True)

@app.route("/")
def home():
    return {"message": "API de Acceso Biométrico funcionando"}

@app.route("/registrar", methods=["POST"])
def registrar():
    nombre = request.json.get("nombre")
    if not nombre:
        return jsonify({"error": "Nombre requerido"}), 400

    cap = cv2.VideoCapture(0)
    count = 0

    person_path = os.path.join(DATASET, nombre)
    os.makedirs(person_path, exist_ok=True)

    while count < 10:
        ret, frame = cap.read()
        if not ret:
            break
        file_path = os.path.join(person_path, f"{count}.jpg")
        cv2.imwrite(file_path, frame)
        count += 1

    cap.release()
    return jsonify({"message": f"Usuario {nombre} registrado"})


@app.route("/acceso", methods=["GET"])
def acceso():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()

    if not ret:
        return jsonify({"error": "No se pudo capturar imagen"}), 500

    # Simulación simple
    usuarios = os.listdir(DATASET)

    if usuarios:
        return jsonify({"acceso": "Permitido", "usuario": usuarios[0]})
    else:
        return jsonify({"acceso": "Denegado"})


if __name__ == "__main__":
    app.run(debug=True)
