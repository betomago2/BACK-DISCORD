# Discord Backend

Este repositorio contiene el código fuente del backend de la aplicación Discord.

## 📝 Índice
- [Instalación](#installation)
- [Estructura del proyecto](#project-structure)
- [Funcionalidades](#functionalities)
- [Tecnologías utilizadas](#technologies)
- [Autores](#authors)

## ⚙️ Instalación <a name = "installation"></a>

Para configurar y ejecutar el backend de la aplicación Discord, sigue estos pasos:

1. **Clonar el repositorio de Backend**
   
   ```bash
   https://github.com/paunicole/TIF-PRUEBA_BACKEND.git
   ```

2. **Crear la base de datos**
   
   Antes de continuar, asegúrate de crear la base de datos que se encuentra en la carpeta [db_for_workbench](db_for_workbench).

4. **Ejecutar el servidor**
   
   Para iniciar el servidor, ejecuta el siguiente comando:

   ```bash
   python run.py
   ```

## 🏛️ Estructura del proyecto <a name = "project-structure"></a>

La estructura del proyecto está organizada de la siguiente manera:

```bash
raíz del proyecto
├───api/
│   ├───controllers/
│   ├───models/
│   ├───routes/
│   ├───__init__.py
│   ├───database.py
├───db_for_workbench/
├───.gitignore
├───config.py
├───README.md
└───run.py
```

## ⚡ Funcionalidades de la Aplicación <a name = "functionalities"></a>

La aplicación Discord Backend cumple con las siguientes funcionalidades:

1. **Registro de Usuarios**:
   - Los usuarios pueden registrarse proporcionando su nombre de usuario, contraseña y otros datos necesarios. La elección de la imagen de perfil está disponible después de la creación del usuario.

2. **Iniciar Sesión**:
   - Los usuarios pueden iniciar sesión en la aplicación. Si el usuario no existe, se mostrará un mensaje sugiriendo el registro.

3. **Interfaz Principal**:
   - La pantalla principal muestra tres columnas:
     
     a. La primera columna lista los servidores a los que pertenece el usuario. Si no pertenece a ninguno, se mostrará un mensaje informativo. Los usuarios pueden seleccionar un servidor para cargar la segunda columna.
     
     b. La segunda columna muestra los canales del servidor seleccionado. Si no hay canales, se muestra un mensaje informativo. Los usuarios pueden seleccionar un canal para cargar la tercera columna o crear un nuevo servidor o canal.
     
     c. La tercera columna muestra los mensajes del chat del canal seleccionado, ordenados cronológicamente. Si no hay mensajes, se mostrará un mensaje informativo. Los usuarios pueden escribir nuevos mensajes en esta columna.
     
4. **Gestión de Mensajes**:
   - Solo el usuario que creó un mensaje puede modificarlo o eliminarlo.

5. **Perfil de Usuario**:
   - Los usuarios pueden ver y actualizar su perfil, incluyendo la imagen de perfil.

## ⛏️ Tecnologías utilizadas <a name = "technologies"></a>
- Python 3.11.4
- Flask 2.3.3
- Flask-Cors 4.0.0
- mysql-connector-python 8.0.33
- python-dotenv 1.0.0

- [Alberto Pallares](https://github.com/betomago2)

