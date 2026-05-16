from django.test import TestCase
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu1 = Menu.objects.create(Title='Pizza', Price=12.5, Inventory=10)
        self.menu2 = Menu.objects.create(Title='Pasta', Price=9.99, Inventory=5)

    def test_get_all(self):
        response = self.client.get('/restaurant/menu/')
        self.assertEqual(response.status_code, 200)
        expected = MenuSerializer([self.menu1, self.menu2], many=True).data
        self.assertEqual(response.json(), expected)
