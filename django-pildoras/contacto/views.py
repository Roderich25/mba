from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import ContactoForm
from django.contrib import messages


class ContactoView(FormView):
    template_name = 'contacto/contacto.html'
    form_class = ContactoForm
    success_url = reverse_lazy('contacto:contacto')

    def form_valid(self, form):
        print("FORM_VALID", self.request.POST)
        nombre = self.request.POST.get('nombre', 'Usuario')
        correo = self.request.POST.get('email', None)
        messages.success(self.request, f'Gracias {nombre}, en breve obtendra una respuesta a su email: {correo}.')
        return HttpResponseRedirect(self.get_success_url())
