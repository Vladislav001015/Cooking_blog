from datetime import datetime
from django import forms


from main_cook.models import Recipe, Image


class RecipeForm(forms.ModelForm):
    created = forms.DateTimeField(initial=datetime.now().strftime("%Y-%m-%d %H:%M"), required=False)
    class Meta:
        model = Recipe
        exclude = ('user',)


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image',)
