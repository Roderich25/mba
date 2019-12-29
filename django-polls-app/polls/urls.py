from django.urls import path
from .views import HomeView, QuestionView, ResultsView, vote

app_name = 'polls'

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('detail/<int:pk>/', QuestionView.as_view(), name='detail'),
    path('results/<int:pk>/', ResultsView.as_view(), name='results'),
    path('vote/<int:q_id>/', vote, name='vote'),
]