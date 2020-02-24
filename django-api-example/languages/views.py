from rest_framework import viewsets, permissions
from .models import Language, Paradigm, Programmer
from .serializers import LanguageSerializer, ParadigmSerializer, ProgrammerSerializer


class LanguageView(viewsets.ModelViewSet):
    serializer_class = LanguageSerializer
    queryset = Language.objects.all()
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ParadigmView(viewsets.ModelViewSet):
    serializer_class = ParadigmSerializer
    queryset = Paradigm.objects.all()


class ProgrammerView(viewsets.ModelViewSet):
    serializer_class = ProgrammerSerializer
    queryset = Programmer.objects.all()