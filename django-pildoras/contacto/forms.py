from django.forms import Form, CharField, Textarea, TextInput


class ContactoForm(Form):
    nombre = CharField(label="Nombre", required=True)
    email = CharField(label="Email", required=True, widget=TextInput(attrs={'autofocus': ''}))
    contenido = CharField(label="Contenido", required=False, widget=Textarea)
