from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(
    UserCreationForm
):
    class Meta:

        model =User 

        filelds = (
            'username',
            'email',
            'password1',
            'password2',
        )