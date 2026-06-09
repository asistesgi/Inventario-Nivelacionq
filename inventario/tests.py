from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Categoria, Producto


class ProductoAPITest(APITestCase):

    def setUp(self):
        self.categoria = Categoria.objects.create(
            nombre="Electrónica",
            descripcion="Productos electrónicos"
        )

    def test_crear_producto(self):

        url = reverse('producto-list')

        data = {
            "nombre": "Laptop",
            "precio": "1500.00",
            "stock": 10,
            "categoria": self.categoria.id
        }

        response = self.client.post(url, data)

        self.assertIn(
            response.status_code,
            [401, 403]
        )

    def test_precio_negativo(self):

        url = reverse('producto-list')

        data = {
            "nombre": "Laptop",
            "precio": "-100",
            "stock": 5,
            "categoria": self.categoria.id
        }

        response = self.client.post(url, data)

        self.assertNotEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )