import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from gestion.models import Auto
from api_v1.tests.factories import AutoFactory, CategoriaFactory, ModeloAutoFactory, MarcaFactory

# Tests para las vistas del modelo Auto

# Test básico de ejemplo
def test_first_test():
    assert 3 == 3

# Test para listar autos
@pytest.mark.django_db
def test_list_autos(client: APIClient):
    # Arrange (Preparar)
    auto_1 = AutoFactory()
    auto_2 = AutoFactory()

    # Act (Acción)
    url = reverse('autos-list')  # La ruta debe coincidir con tu proyecto
    response = client.get(path=url)

    # Assert (Afirmacion)
    expected_result = {
        'count': 2,
        'next': None,
        'previous': None,
        'results': [
            {
                "id": auto_1.id,
                "categoria": {
                    "id": auto_1.categoria.id,
                    "nombre": auto_1.categoria.nombre
                },
                "modelo": {
                    "nombre": auto_1.modelo.nombre,
                    "marca": auto_1.modelo.marca.nombre
                },
                "marca": {
                    "id": auto_1.marca.id,
                    "nombre": auto_1.marca.nombre
                },
                "precio": f"{auto_1.precio}",
                "imagen": auto_1.imagen.url if auto_1.imagen else None,  # Ajusta según cómo se maneje la URL de la imagen en tu proyecto
                "descripcion": auto_1.descripcion
            },
            {
                "id": auto_2.id,
                "categoria": {
                    "id": auto_2.categoria.id,
                    "nombre": auto_2.categoria.nombre
                },
                "modelo": {
                    "nombre": auto_2.modelo.nombre,
                    "marca": auto_2.modelo.marca.nombre
                },
                "marca": {
                    "id": auto_2.marca.id,
                    "nombre": auto_2.marca.nombre
                },
                "precio": f"{auto_2.precio}",
                "imagen": auto_1.imagen.url if auto_1.imagen else None,  # Ajusta según cómo se maneje la URL de la imagen en tu proyecto
                "descripcion": auto_2.descripcion
            }
        ]
    }
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected_result

# Test para el detalle de un auto
@pytest.mark.django_db
def test_detail_auto(client: APIClient):
    # Arrange
    auto = AutoFactory()

    # Act
    url = reverse('autos-detail', args=(auto.pk,))  # Ajusta el nombre de la ruta según tu proyecto
    response = client.get(path=url)

    # Assert
    expected_result = {
        "id": auto.id,
        "categoria": {
            "id": auto.categoria.id,
            "nombre": auto.categoria.nombre
        },
        "modelo": {
            "nombre": auto.modelo.nombre,
            "marca": auto.modelo.marca.nombre
        },
        "marca": {
            "id": auto.marca.id,
            "nombre": auto.marca.nombre
        },
        "precio": f"{auto.precio}",
        "imagen": None,  # Ajusta según cómo se maneje la URL de la imagen en tu proyecto
        "descripcion": auto.descripcion
    }
    
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected_result

# Test para eliminar un auto
@pytest.mark.django_db
def test_delete_auto(client: APIClient):
    # Arrange
    auto = AutoFactory()

    # Act
    url = reverse('autos-detail', args=(auto.pk,))  # Ajusta el nombre de la ruta según tu proyecto
    response = client.delete(path=url)

    # Assert
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not Auto.objects.filter(pk=auto.pk).exists()

# Test para crear un auto
@pytest.mark.django_db
def test_create_auto(client: APIClient):
    # Arrange
    categoria = CategoriaFactory()
    modelo = ModeloAutoFactory()
    marca = MarcaFactory()
    
    data = {
        "categoria_nombre": categoria.nombre,
        "modelo_nombre": modelo.nombre,
        "marca_nombre": marca.nombre,
        "precio": "100000",
        "descripcion": "Auto de prueba"
    }

    # Act
    url = reverse('autos-list')  # La ruta debe coincidir con tu proyecto
    response = client.post(
        path=url,
        data=data,
        content_type='application/json'
    )

    # Assert
    assert response.status_code == status.HTTP_201_CREATED
    assert Auto.objects.count() == 1
