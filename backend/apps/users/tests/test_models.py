from django.contrib.auth import get_user_model
from django.test import TestCase

User = get_user_model()


def create_user(
    email="test@email.com",
    password="testpass123",
    is_active=False,
):
    return User.objects.create_user(
        email=email,
        password=password,
        is_active=is_active,
    )


def create_superuser(
    email="superuser@email.com",
    password="testpass123",
    is_active=True,
    is_staff=True,
    is_superuser=True,
):
    return User.objects.create_superuser(
        email=email,
        password=password,
        is_active=is_active,
        is_superuser=is_superuser,
        is_staff=is_staff,
    )


class UserManagerTests(TestCase):
    def test_create_user(self):
        """Test creating a user is successful."""
        user = create_user(email="goood@email.com")

        self.assertEquals(user.email, "goood@email.com")

        self.assertFalse(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        """Test create super user."""
        admin_user = get_user_model().objects.create_superuser(email="admin@gmail.com", password="testpass123")
        self.assertEqual(admin_user.email, "admin@gmail.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

    def test_delete_user(self):
        """Test delete user."""
        user = create_user("goood@email.com")
        user.delete()
        user_model = User.objects.filter(email="goood@email.com").exists()
        self.assertFalse(user_model)

    def test_create_user_error(self):
        """Test create user error."""

        try:
            create_user("goood@email")
        except ValueError as e:
            self.assertEqual(e.args[0], "You must provide a valid email address.")

        try:
            create_user(email=None)
        except ValueError as e:
            self.assertEqual(e.args[0], "User must have an email address.")

    def test_create_superuser_error(self):
        """Test create super user error."""

        try:
            create_superuser(is_staff=False)
        except ValueError as e:
            self.assertEqual(e.args[0], "Superuser must have is_staff=True.")

        try:
            create_superuser(is_superuser=False)
        except ValueError as e:
            self.assertEqual(e.args[0], "Superuser must have is_superuser=True.")

        try:
            create_superuser(password=None)
        except ValueError as e:
            self.assertEqual(e.args[0], "Superuser must have a password.")

        try:
            create_superuser(email=None)
        except ValueError as e:
            self.assertEqual(e.args[0], "Superuser must have an email address.")


class UserModelTests(TestCase):
    def test_str(self):
        """Test user string representation."""
        user = create_user("goood@email.com")
        self.assertEqual(str(user), "goood@email.com")
