from django import forms
from .models import Comida

class ComidaForm(forms.ModelForm):

    class Meta:
        model = Comida
        fields = ('descricao', 'preco',)
