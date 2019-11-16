from django import forms
from .models import Comentario


class BuscarForm(forms.Form):
    palabras = forms.CharField()


class EmailPostForm(forms.Form):
    nombre = forms.CharField(max_length=25)
    email = forms.EmailField()
    para = forms.EmailField()
    comentarios = forms.CharField(required=False,
                               widget=forms.Textarea)


class ComentarioForm(forms.ModelForm):

    class Meta:
        model = Comentario
        fields = ('nombre', 'email', 'comentario')
