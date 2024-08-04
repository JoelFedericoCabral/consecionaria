# Concesionaria de Autos

Este proyecto es un sistema de gestión para una concesionaria de autos, desarrollado con Django. Permite la gestión de autos, ventas, clientes, empleados, servicios y más.

## Tabla de Contenidos

- [Instalación](#instalación)
- [Uso](#uso)
- [Características](#características)
- [Contacto](#contacto)

## Instalación

### Requisitos Previos

- Python 3.10 o superior
- Django 5.0.7
- Entorno virtual (recomendado)

### Configuración del Entorno

1. Clona este repositorio:

    ```bash
    git clone https://github.com/JoelFedericoCabral/consecionaria.git
    ```

2. Navega al directorio del proyecto:

    ```bash
    cd concesionaria
    ```

3. Crea y activa un entorno virtual:

    ```bash
    python -m venv env
    source env/bin/activate  # En Windows: env\Scripts\activate
    ```

4. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

5. Realiza las migraciones de la base de datos:

    ```bash
    python manage.py migrate
    ```

6. Carga datos iniciales si es necesario (opcional):

    ```bash
    python manage.py loaddata initial_data.json
    ```

## Uso

### Ejecutar el Servidor de Desarrollo

Para iniciar el servidor de desarrollo, ejecuta:

```bash
python manage.py runserver
```


### Accede al sistema desde tu navegador web en:

    http://127.0.0.1:8000


## Usuarios de Prueba
Para facilitar la evaluación del sistema, hemos creado usuarios de prueba con diferentes roles. Puedes utilizar estas credenciales para acceder y evaluar las funcionalidades y restricciones implementadas para cada tipo de usuario.

### Usuario Staff (Administrador)
- Nombre de usuario: admin
- Contraseña: administrador


Este usuario tiene permisos completos y acceso a todas las funcionalidades del sistema, incluyendo la gestión de clientes, ventas, empleados y proveedores.


### Usuario Regular (Cliente)
- Nombre de usuario: probando
- Contraseña: probandoAndo


Este usuario tiene permisos limitados y puede interactuar con funcionalidades básicas y cumliendo con las desciptas en las consignas de la EFI.


Características
Gestión de Autos: Crear, actualizar, eliminar y visualizar autos.
Gestión de Clientes: Registro y administración de clientes.
Gestión de Ventas: Proceso de ventas de autos.
Gestión de Empleados: Administración del personal.
Gestión de Proveedores: Control de proveedores de autos.
Gestión de Servicios: Servicios adicionales ofrecidos por la concesionaria.
Citas: Programación de citas para servicios.
Financiamiento: Opciones de financiamiento para clientes.
Autenticación y Autorización: Sistema de login y registro con permisos basados en roles.


Contacto
Para cualquier consulta o comentario, puedes contactarme a través de mi correo: f.cabral@itecriocuarto.org.ar

