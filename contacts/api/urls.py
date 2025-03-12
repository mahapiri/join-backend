from os import path
from contacts.api.views import ContactDetailViewSet


urlpatterns = [
    path('<int:pk>/', ContactDetailViewSet.as_view(), name='contact-detail'),
]