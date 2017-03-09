from django.contrib.auth.forms import UserCreationForm
from .models import MyUser,Etudiant
from django.forms import ModelForm
class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ("email","first_name","last_name","is_sick")


class EtudiantForm(ModelForm):
    class Meta:
        model = Etudiant
        exclude = ("user",)
