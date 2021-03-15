from django.db.models import Model, CharField, TextField, DateTimeField


class Contacto(Model):
    nombre = CharField(max_length=128)
    email = CharField(max_length=128)
    contenido = TextField()
    fecha = DateTimeField()
