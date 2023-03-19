from django.test import TestCase
from .models import Item


class TestItem(TestCase):

    def test_done_defaults_to_false(self):
        item = Item.objects.create(name='Test Model')
        self.assertFalse(item.done)

    def test_item_str_method_returns_name(self):
        item = Item.objects.create(name="Todo List Item")
        # Check the __str__(self) model method returns the name
        self.assertEqual(str(item), 'Todo List Item')
