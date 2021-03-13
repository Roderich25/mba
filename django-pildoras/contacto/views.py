from django.views.generic import FormView
from .forms import ContactoForm


class ContactoView(FormView):
    template_name = 'contacto/contacto.html'
    form_class = ContactoForm
    # initial = {'nombre': 'tu nombre', 'email': 'tu correo', 'contenido': 'tu mensaje'}
    success_url = "/contacto/"
