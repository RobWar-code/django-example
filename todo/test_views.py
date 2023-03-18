from django.test import TestCase
from .models import Item


# Create your tests here.
class TestViews(TestCase):

    def test_get_to_do_list(self):
        # Simulate getting the home page
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("todo/todo-list.html")

    def test_get_add_item(self):
        response = self.client.get("/add/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("todo/add_item.html")

    def test_get_edit_item(self):
        # Get a valid item id
        item = Item.objects.create(name="Test Todo Item")
        # Note that the view request includes the item_id
        response = self.client.get(f'/edit/{item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("todo/edit_item.html")

    def test_can_add_item(self):
        # Perform an add record operation
        response = self.client.post("/add/", {'name': 'Test Added Item'})
        self.assertRedirects(response, "/")

    def test_can_delete_item(self):
        item = Item.objects.create(name='Test Todo Item')
        response = self.client.get(f'/delete/{item.id}')
        self.assertRedirects(response, "/")
        existing_items = Item.objects.filter(id=item.id)
        self.assertEqual(len(existing_items), 0)

    # def test_can_toggle_item(self):
        item = Item.objects.create(name='Test Todo Item', done=True)
        response = self.client.get(f'/toggle/{item.id}')
        self.assertRedirects(response, "/")
        updated_item = Item.objects.get(id=item.id)
        self.assertFalse(updated_item.done)
