from  django.urls import path
from catalog.views import home, contacts, thank
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'catalog'

urlpatterns = [
    path('', home, name = 'home'),
    path('contacts/', contacts, name = 'contacts'),
    path('thank_you/', thank, name = 'thank')
    ] + staticfiles_urlpatterns()