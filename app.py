# 1. Importar la clase Flask desde la librería flask
from flask import Flask

# 2. Crear una instancia de la aplicación Flask
# __name__ es una variable especial en Python que representa el nombre del módulo actual.
# Flask la usa para saber dónde buscar recursos como plantillas y archivos estáticos.
app = Flask(__name__)

# 3. Definir una ruta para la página principal ('/')
# El decorador @app.route('/') le dice a Flask que cuando alguien visite
# la dirección raíz del sitio web, debe ejecutar la función 'saludo'.
@app.route('/')
def saludo():
    # 4. La función devuelve el texto (o HTML) que se mostrará en el navegador.
    # Usamos una etiqueta <h1> de HTML para que el texto aparezca como un encabezado grande.
    return '<h1>Os saluda Andrés desde jenkins</h1>'
   

# 5. Comprobar si el script se está ejecutando directamente
# Esto es estándar en Python para asegurarse de que el código dentro de este bloque
# solo se ejecute cuando corres el script directamente (python app.py),
# y no cuando lo importas en otro script.
if __name__ == '__main__':
    # 6. Ejecutar la aplicación en un servidor de desarrollo local.
    # debug=True activa el modo de depuración, que es útil durante el desarrollo
    # porque reinicia automáticamente el servidor si cambias el código y
    # muestra errores detallados en el navegador.
    # Por defecto, se ejecutará en http://127.0.0.1:5000/
    app.run(host="0.0.0.0", port=5000, debug=True)
