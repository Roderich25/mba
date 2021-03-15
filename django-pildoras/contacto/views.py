from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import ContactoForm
from django.contrib import messages
from django.core.mail import send_mail
from django.utils import timezone
from contacto.models import Contacto


class ContactoView(FormView):
    template_name = 'contacto/contacto.html'
    form_class = ContactoForm
    success_url = reverse_lazy('contacto:contacto')

    def form_valid(self, form):
        nombre = self.request.POST.get('nombre', 'Usuario')
        correo = self.request.POST.get('email', None)
        contenido = self.request.POST.get('contenido', None)
        dte = timezone.now()

        c = Contacto(nombre=nombre, email=correo, contenido=contenido, fecha=dte)
        c.save()

        messages.success(self.request, f'Gracias {nombre}, en breve obtendra una respuesta a su email: {correo}.')

        send_mail(subject="Thanks for contacting us",
                  message=f"You contacted us on {dte.strftime('%B/%d/%Y')} about {contenido}.\nYou'll receive an answer soon.",
                  from_email="rodrigo@contacto.com",
                  recipient_list=[correo],
                  fail_silently=False)

        return HttpResponseRedirect(self.get_success_url())
