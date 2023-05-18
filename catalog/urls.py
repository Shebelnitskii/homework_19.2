from  django.urls import path
from catalog.views import index
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', index)
    ] + staticfiles_urlpatterns()