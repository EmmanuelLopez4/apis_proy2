import os
import cv2
import shutil

DATASET = "dataset"


class BiometricoService:

    @staticmethod
    def registrar_usuario(nombre, cantidad=10):
        if not nombre or nombre.strip() == "":
            raise ValueError("Nombre requerido")

        os.makedirs(DATASET, exist_ok=True)

        ruta = os.path.join(DATASET, nombre)

        if os.path.exists(ruta):
            shutil.rmtree(ruta)

        os.makedirs(ruta)

        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            raise RuntimeError("No se pudo abrir la cámara")

        count = 0

        while count < cantidad:
            ret, frame = cap.read()
            if not ret:
                break

            file_path = os.path.join(ruta, f"{count}.jpg")
            cv2.imwrite(file_path, frame)
            count += 1

        cap.release()

        return {
            "mensaje": f"Usuario {nombre} registrado con {count} imágenes"
        }

    @staticmethod
    def validar_acceso():
        os.makedirs(DATASET, exist_ok=True)

        usuarios = [
            u for u in os.listdir(DATASET)
            if os.path.isdir(os.path.join(DATASET, u))
        ]

        if not usuarios:
            return {
                "acceso": "Denegado",
                "mensaje": "No hay usuarios registrados"
            }

        return {
            "acceso": "Permitido",
            "usuario": usuarios[0]
        }

    @staticmethod
    def eliminar_usuario(nombre):
        ruta = os.path.join(DATASET, nombre)

        if not os.path.exists(ruta):
            return {"mensaje": "Usuario no existe"}

        shutil.rmtree(ruta)

        return {"mensaje": f"Usuario {nombre} eliminado"}