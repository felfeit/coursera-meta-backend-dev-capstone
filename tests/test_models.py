from django.test import TestCase
from restaurant.models import Menu

class MenuModelTest(TestCase):
    def test_str_representation(self):
        menu = Menu.objects.create(Title='IceCream', Price=80, Inventory=100)
        self.assertEqual(str(menu), 'IceCream : 80')
