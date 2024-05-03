from django.test import TestCase
from ..forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class UserChangeFormTest(TestCase):
    def test_valid_user_change_form(self):
        user = User.objects.create_user(email='test@example.com', password='Pass1234')
        form_data = {'email': 'changed2@example.com', 'date_joined': user.date_joined}
        form = UserChangeForm(instance=user, data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_user_change_form(self):
        user = User.objects.create_user(email='test@example.com', password='Pass1234')
        form_data = {'email': 'test@example.com'}  # Trying to change email to an existing one
        form = UserChangeForm(instance=user, data=form_data)
        self.assertFalse(form.is_valid())

class UserCreationFormTest(TestCase):
    def test_valid_user_creation_form(self):
        form_data = {'email': 'newuser@example.com', 'password1': 'Pass12345', 'password2': 'Pass12345'}
        form = UserCreationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_user_creation_form(self):
        User.objects.create_user(email='existing@example.com', password='Pass1234')
        form_data = {'email': 'existing@example.com', 'password1': 'Pass1234', 'password2': 'Pass1234'}
        form = UserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
