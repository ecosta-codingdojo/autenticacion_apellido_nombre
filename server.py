"""Server app."""

# Importar la aplicación
from app import app

# Controladores de usuarios
from app.controllers.usuarios import index, dashboard, registrar_usuario, iniciar_sesion, cerrar_sesion


# Ejecutar el servidor
if __name__ == "__main__":
    app.run(debug=True, port=5000)
