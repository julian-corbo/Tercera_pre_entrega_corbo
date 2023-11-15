from django.test import TestCase

from blog.models import Cafeterias


class CafeteriasTests(TestCase):
   """En esta clase van todas las pruebas del modelo Cafeterias."""

   def test_creacion_cafeteria(self):
       # caso uso esperado
       cafeteria = Cafeterias(nombre="Culto", direccion="Bartolomé Mitre 1270")
       cafeteria.save()

       # Compruebo que el curso fue creado y la data fue guardad correctamente
       self.assertEqual(Cafeterias.objects.count(), 1)
       self.assertEqual(cafeteria.nombre, "Culto")
       self.assertEqual(cafeteria.direccion, "Bartolomé Mitre 1270")


