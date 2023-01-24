from django.urls import path
from templating.views import home_page, contacts_page
from templating.apps import TemplatingConfig

app_name = TemplatingConfig.name

urlpatterns = [
    path('', home_page, name='home'),
    path('contacts/', contacts_page, name='contacts')
]