from rest_framework.routers import SimpleRouter
from django.urls import path
from .views import PostViewSet, UserViewSet  # PostList, PostDetail, UserList, UserDetail

router = SimpleRouter()
router.register('users', UserViewSet, base_name='users')
router.register('', PostViewSet, base_name='posts')

urlpatterns = router.urls

# urlpatterns = [
# path('users/', UserList.as_view()),
# path('users/<int:pk>/', UserDetail.as_view()),
# path('<int:pk>/', PostDetail.as_view()),
# path('', PostList.as_view()),
# ]
