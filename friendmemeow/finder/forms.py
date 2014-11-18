from django import forms

# from .models import Kitty
from finder.models import Kitty


class AddCat(forms.ModelForm):

    class Meta:
        model = Kitty
        fields = ('name', 'location', 'gender', 'age', 'breed', 'about', 'status','photo')
