# app.py
import os
import requests
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Crear la aplicación Flask
app = Flask(__name__)

# Obtener el token de la API desde las variables de entorno
API_TOKEN = os.getenv('API_TOKEN')
API_URL = 'https://api.apis.net.pe/v2/reniec/dni'

# Ruta para servir la página HTML principal
@app.route('/')
def index():
    """
    Sirve la página HTML principal (index.html).
    """
    # Usaremos render_template para servir un archivo HTML que crearemos luego
    return render_template('index.html')

# Ruta para consultar el DNI (nuestra API interna)
@app.route('/consultar-dni', methods=['POST'])
def consultar_dni():
    """
    Endpoint que recibe un DNI, consulta la API externa y devuelve los datos.
    Espera recibir un JSON con la clave 'dni'.
    """
    # Verificar que se recibió un JSON
    if not request.is_json:
        return jsonify({"error": "La solicitud debe ser de tipo JSON"}), 400

    data = request.get_json()
    dni = data.get('dni')

    # Validar que se recibió el DNI
    if not dni:
        return jsonify({"error": "Número de DNI no proporcionado"}), 400

    # Validar que el token está configurado
    if not API_TOKEN:
        return jsonify({"error": "Token de API no configurado en el servidor"}), 500

    # Preparar la solicitud a la API externa
    headers = {
        'Authorization': f'Bearer {API_TOKEN}',
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }
    params = {
        'numero': dni
    }

    try:
        # Realizar la solicitud GET a la API de apis.net.pe
        response = requests.get(API_URL, headers=headers, params=params, timeout=10) # Timeout de 10 segundos

        # Verificar si la solicitud fue exitosa (código 2xx)
        response.raise_for_status() # Lanza una excepción para códigos de error HTTP (4xx o 5xx)

        # Devolver la respuesta JSON de la API externa
        datos_persona = response.json()
        return jsonify(datos_persona)

    except requests.exceptions.RequestException as e:
        # Manejar errores de conexión, timeout, o códigos HTTP de error
        error_message = f"Error al consultar la API externa: {e}"
        status_code = 500 # Error interno del servidor por defecto
        if e.response is not None:
             # Si hay una respuesta del servidor de la API externa, usar su código de estado
            status_code = e.response.status_code
            try:
                # Intentar obtener el mensaje de error del JSON de la respuesta
                 error_detail = e.response.json().get('message', str(e))
                 error_message = f"Error de la API externa ({status_code}): {error_detail}"
            except ValueError: # Si la respuesta no es JSON válido
                 error_message = f"Error de la API externa ({status_code}): {e.response.text}"

        print(f"Error: {error_message}") # Imprimir el error en la consola del servidor Flask
        return jsonify({"error": "No se pudo obtener la información del DNI.", "detalle": error_message}), status_code

    except Exception as e:
        # Manejar cualquier otro error inesperado
        print(f"Error inesperado: {e}")
        return jsonify({"error": "Ocurrió un error inesperado en el servidor."}), 500

# Iniciar el servidor Flask si este archivo se ejecuta directamente
if __name__ == '__main__':
    # debug=True es útil para desarrollo, pero debe desactivarse en producción
    # host='0.0.0.0' permite acceder desde otros dispositivos en la misma red
    app.run(host='0.0.0.0', port=5000, debug=True)