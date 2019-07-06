from django.test import TestCase
from django.utils import timezone
from .models import Todo
from .forms import TodoForm

# Create your tests here.
class TodoTestCase(TestCase):

    def setUp(self):
        form_data = {
            'title': "Test",
            'description': "Test description",
            'status': 0
        }
        form_todo = TodoForm(data=form_data)
        form_todo.save()
    
    def test_create_todo(self):
        form_data = {
            'title': "Test2",
            'description': "Test2 description",
            'status': 0
        }
        form_todo = TodoForm(data=form_data)
        form_todo.save()
        todo = Todo.objects.get(title="Test2")
        self.assertEqual(todo.title, "Test2")
    
    def test_todo_no_title(self):
        form_data = {
            'title': "",
            'description': "Test description",
            'status': 0
        }
        form_todo = TodoForm(data=form_data)
        self.assertFalse(form_todo.is_valid())

    def test_todo_no_description(self):
        form_data = {
            'title': "Test2",
            'description': "",
            'status': 0
        }
        form_todo = TodoForm(data=form_data)
        self.assertTrue(form_todo.is_valid())
    
    def test_todo_wrong_status(self):
        form_data = {
            'title': "Test2",
            'description': "Test2 description",
            'status': 100
        }
        form_todo = TodoForm(data=form_data)
        self.assertFalse(form_todo.is_valid())
    
    def test_todo_edit_title(self):
        todo = Todo.objects.get(title="Test")
        todo.title = "Test100"
        todo.save()
        todo = Todo.objects.get(title="Test100")
        self.assertEqual(todo.title, "Test100")
    
    def test_todo_edit_description(self):
        todo = Todo.objects.get(title="Test")
        todo.description = "test test test"
        todo.save()
        todo = Todo.objects.get(title="Test")
        self.assertEqual(todo.description, "test test test")
    
    def test_todo_edit_status(self):
        todo = Todo.objects.get(title="Test")
        todo.status = 1
        todo.save()
        todo = Todo.objects.get(title="Test")
        self.assertEqual(todo.status, 1)
    
    def test_delete_todo(self):
        form_data = {
            'title': "Test2",
            'description': "Test2 description",
            'status': 0
        }
        form_todo = TodoForm(data=form_data)
        form_todo.save()
        Todo.objects.get(title="Test2").delete()
        try:
            Todo.objects.get(title="Test2")
            self.fail("To-do deleted")
        except BaseException:
            pass
