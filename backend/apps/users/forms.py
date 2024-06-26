from django import forms
from django.contrib.auth import forms as admin_forms, get_user_model

User = get_user_model()


class UserChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User


class UserCreationForm(admin_forms.UserCreationForm):
    class Meta(admin_forms.UserCreationForm.Meta):
        model = User
        fields = ("email",)

    error_messages = {
        "duplicate_email": "A user with that email already exists.",
    }

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(self.error_messages["duplicate_email"])
        return email
