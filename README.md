# Concesionaria de Autos
Este proyecto es un sistema de gestión para una concesionaria de autos, desarrollado con Django. Permite la gestión de autos, ventas, clientes, empleados, servicios y más. Además, ahora incluye una API REST que permite interactuar con el sistema de manera programática.

## Tabla de Contenidos
- Instalación
- Uso
- API REST
- Usuarios de Prueba
- Características
- Contacto
- Mejoras

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
    cd consecionaria
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


## Uso

### Ejecutar el Servidor de Desarrollo

Para iniciar el servidor de desarrollo, ejecuta:

```bash
python manage.py runserver
```


### Accede al sistema desde tu navegador web en:

    http://127.0.0.1:8000

## API REST
Este proyecto ahora incluye una API REST que permite realizar operaciones de gestión para los diferentes modelos del sistema (autos, marcas, usuarios, clientes, etc.). Puedes interactuar con la API utilizando herramientas como Postman, Thunder Client, curl, entre otros.

## Documentación de la API
Documentación de la API
Para una descripción detallada de los endpoints, incluyendo los parámetros requeridos y las respuestas posibles, se ha implementado documentación automática utilizando Swagger y ReDoc. Puedes acceder a la documentación en los siguientes enlaces:

- Swagger UI: http://127.0.0.1:8000/swagger/
- ReDoc: http://127.0.0.1:8000/redoc/

Estas interfaces te permiten explorar la API, ver ejemplos de solicitudes y respuestas, y probar los endpoints directamente desde tu navegador.


## Usuarios de Prueba
Para facilitar la evaluación del sistema, he creado usuarios de prueba con diferentes roles. Puedes utilizar estas credenciales para acceder y evaluar las funcionalidades y restricciones implementadas para cada tipo de usuario.

### Usuario Staff (Administrador)
- Nombre de usuario: admin
- Contraseña: administrador

Este usuario tiene permisos completos y acceso a todas las funcionalidades del sistema, incluyendo la gestión de clientes, ventas, empleados y proveedores. Siempre respetando lo que pedia la consigna de la EFI en cuanto al administrador con rol de staff.


### Usuario Regular (Cliente No Staff)
- Nombre de usuario: probando
- Contraseña: probandoAndo

Este usuario tiene permisos limitados y puede interactuar con funcionalidades básicas y cumpliendo con las descriptas en las consignas de la EFI.


## Características
- Gestión de Autos: Crear, actualizar, eliminar y visualizar autos.
- Gestión de Clientes: Registro y administración de clientes.
- Gestión de Ventas: Proceso de ventas de autos.
- Gestión de Empleados: Administración del personal.
- Gestión de Proveedores: Control de proveedores de autos.
- Gestión de Servicios: Servicios adicionales ofrecidos por la concesionaria.
- Citas: Programación de citas para servicios.
- Financiamiento: Opciones de financiamiento para clientes.
- Autenticación y Autorización: Sistema de login y registro con permisos basados en roles.
- API REST: Interfaz para gestionar los modelos de la concesionaria de manera programática.
- Documentación de API: Implementada usando Swagger y ReDoc para facilitar la integración y desarrollo con la API.
- Internacionalización: Soporte multilingüe en la interfaz, con opciones de cambio de idioma.


## Contacto
Para cualquier consulta o comentario, puedes contactarme a través de mi correo: 
- f.cabral@itecriocuarto.org.ar


## Mejoras
Aunque el sistema de gestión de concesionaria de autos está completamente funcional y cumple con los requisitos de la evaluación final, hay varias mejoras que podrían implementarse en el futuro para mejorar la experiencia del usuario y la funcionalidad del sistema. Algunas ideas incluyen:

- **Simulación de Financiamiento Real:** Mejorar el módulo de financiamiento para permitir a los usuarios simular diferentes planes de financiamiento con opciones de personalización como tasa de interés, plazo y cuota inicial.

- **Interfaz de Usuario Mejorada:** Optimizar la apariencia y el diseño de la interfaz para proporcionar una experiencia de usuario más intuitiva y atractiva, utilizando tecnologías como Bootstrap 5 o frameworks de frontend modernos como React, entre otros. 

- **Sistema de Notificaciones:** Implementar un sistema de notificaciones para mantener a los usuarios informados sobre actualizaciones importantes, como nuevos autos disponibles, recordatorios de citas, y más.

- **Búsqueda Avanzada:** Añadir capacidades de búsqueda avanzada que permitan a los usuarios filtrar autos, clientes y otros datos por múltiples criterios, mejorando la facilidad de uso y la accesibilidad de la información.

- **Internacionalización:** Ampliar el soporte multilingüe para facilitar el acceso al sistema a usuarios de diferentes regiones y mejorar la adaptabilidad del sistema en un entorno internacional.

- **Soporte para Dispositivos Móviles:** Asegurar que la aplicación sea completamente responsive y accesible desde dispositivos móviles, proporcionando una experiencia fluida en teléfonos y tablets.

Estas mejoras no solo incrementarán el valor del sistema, sino que también ofrecerán oportunidades para expandir el alcance y la funcionalidad del proyecto.
