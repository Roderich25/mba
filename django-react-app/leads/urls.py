from rest_framework import routers
from leads.api import LeadViewset

router = routers.DefaultRouter()
router.register('api/leads', LeadViewset, 'leads')

urlpatterns = router.urls