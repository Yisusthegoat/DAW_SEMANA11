from django.test import TestCase
from django.urls import reverse

from .models import Producto


class PaginasCatalogoTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.producto = Producto.objects.create(
            nombre="teclado mecanico",
            descripcion="Teclado compacto para oficina y trabajo diario.",
            precio="189.90",
            stock=12,
        )

    def test_inicio_muestra_resumen_y_producto(self):
        respuesta = self.client.get(reverse("home"))

        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, "Todo en orden")
        self.assertContains(respuesta, "Teclado Mecanico")

    def test_catalogo_lista_productos_y_stock(self):
        respuesta = self.client.get(reverse("catalogo"))

        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, "Catálogo de")
        self.assertContains(respuesta, "12 unidades")
        self.assertContains(respuesta, "189.90")

    def test_producto_tiene_representacion_legible(self):
        self.assertEqual(str(self.producto), "teclado mecanico")
