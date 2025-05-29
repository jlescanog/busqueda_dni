# 🔍 Consulta DNI Perú

![Banner](https://img.shields.io/badge/Estado-Funcional-brightgreen)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-3.1.1-lightgrey)

Una aplicación web simple y eficiente para consultar datos personales a partir de un número de DNI peruano, utilizando la API de [apis.net.pe](https://apis.net.pe).

![Captura de pantalla de la aplicación](https://via.placeholder.com/800x400?text=Consulta+DNI+Per%C3%BA)

## 📋 Características

- Interfaz web intuitiva y responsive
- Validación de formato de DNI (8 dígitos)
- Consulta en tiempo real a la API de RENIEC
- Visualización clara de los resultados
- Manejo adecuado de errores y excepciones

## 🚀 Instalación y Configuración

### Requisitos Previos

- Python 3.8 o superior
- Conexión a Internet
- Token de API de [apis.net.pe](https://apis.net.pe)

### Pasos para la Instalación

#### En Windows

1. **Clonar el repositorio**

   ```powershell
   git clone https://github.com/tu-usuario/busqueda_dni.git
   cd busqueda_dni
   ```

2. **Crear un entorno virtual**

   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Instalar dependencias**

   ```powershell
   pip install -r requirements.txt
   ```

4. **Configurar variables de entorno**

   Copia el archivo `.env.example` a `.env` y edítalo para agregar tu token de API:

   ```powershell
   copy .env.example .env
   # Edita el archivo .env con tu editor preferido
   # API_TOKEN=tu-token-aquí
   ```

5. **Ejecutar la aplicación**

   ```powershell
   python app.py
   ```

#### En Linux/macOS

1. **Clonar el repositorio**

   ```bash
   git clone https://github.com/tu-usuario/busqueda_dni.git
   cd busqueda_dni
   ```

2. **Crear un entorno virtual**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instalar dependencias**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar variables de entorno**

   ```bash
   cp .env.example .env
   # Edita el archivo .env con tu editor preferido
   # API_TOKEN=tu-token-aquí
   ```

5. **Ejecutar la aplicación**

   ```bash
   python app.py
   ```

## 🌐 Uso de la Aplicación

1. Abre tu navegador y visita `http://localhost:5000`
2. Ingresa un número de DNI válido (8 dígitos)
3. Haz clic en "Consultar"
4. Los resultados se mostrarán en la pantalla

## 📝 Estructura del Proyecto

```
busqueda_dni/
├── app.py                # Aplicación principal Flask
├── requirements.txt      # Dependencias del proyecto
├── .env                  # Variables de entorno (no incluido en el repositorio)
├── .env.example          # Ejemplo de configuración de variables de entorno
└── templates/
    └── index.html        # Interfaz de usuario
```

## 🔑 Obtener un Token de API

Para utilizar esta aplicación, necesitas un token de API de [apis.net.pe](https://apis.net.pe):

1. Regístrate en [apis.net.pe](https://apis.net.pe)
2. Adquiere un plan que incluya acceso a la API de RENIEC
3. Genera un token de API en tu panel de control
4. Copia el token en tu archivo `.env`

## 🛠️ Despliegue en Producción

Para un entorno de producción, se recomienda:

1. Desactivar el modo debug en `app.py`:
   ```python
   app.run(host='0.0.0.0', port=5000, debug=False)
   ```

2. Utilizar un servidor WSGI como Gunicorn:
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 app:app
   ```

3. Configurar un proxy inverso como Nginx o Apache

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## 👨‍💻 Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request para sugerir cambios o mejoras.

---

⭐ Si encuentras útil este proyecto, ¡no dudes en darle una estrella en GitHub!
