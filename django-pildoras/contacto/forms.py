from django.forms import Form, CharField


class ContactoForm(Form):
    nombre = CharField(label="Nombre", required=True)
    email = CharField(label="Email", required=True)
    contenido=CharField(label="Contenido", required=False)
