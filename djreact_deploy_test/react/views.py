from django.views.generic import TemplateView
import os
from django.conf import settings


class IndexView(TemplateView):
    template_name = 'react/index.html'
