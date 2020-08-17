
from django.contrib import admin
from django.urls import path
from core.views import TestView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TestView.as_view(), name='test'),
]