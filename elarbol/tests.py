import unittest
from elarbol.models import Producto
from elarbol.models import User
from django.contrib import messages

class testProducto(unittest.TestCase):




    def test_eliminar_objeto(self):
        producto = Producto.objects.create(nombre_producto='Leche',
                                       precio='1000',
                                       stock= '1',
                                       descripcion='nada',
                                       activo='1',
                                       foto_producto= ''
                                     )
        producto.save()
        self.assertTrue(producto, True)

    def test_crear_objeto(self):
        producto = Producto.objects.create(nombre_producto='Leche',
                                       precio='1000',
                                       stock= '1',
                                       descripcion='nada',
                                       activo='1',
                                       foto_producto= ''
                                     )
        producto.save()
        self.assertTrue(producto, True)


    def test_volver_a_crear_objeto(self):
        producto = Producto.objects.create(nombre_producto='Caja de Almendras',
                                           precio='10000',
                                           stock='',
                                           descripcion='nada',
                                           activo='1',
                                           foto_producto=''
                                           )
        producto.save()
        self.assertTrue(producto, True)







class testUser(unittest.TestCase):

    def test_crear_user(self):
        user = User.objects.create(username='testPrueba',
                                       email='abc@gmail.com',
                                       password='clave.123'
                                     )
        user.save()
        self.assertTrue(user, True)

    def test_eliminar_user(self):
         user = User.objects.get(username='testPrueba')

         user.delete()


         self.assertTrue(user, True)

    def volver_a_crear_user(self):
        user = User.objects.create(username='testPrueba',
                                       email='abc@gmail.com',
                                       password='clave.123'
                                     )
        user.save()
        self.assertTrue(user, True)