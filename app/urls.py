from django.urls import path

from app.views import Index, ContactCreate


urlpatterns = [
    path('', Index.as_view(), name="home"),
    path('contact/', ContactCreate.as_view(), name="contact"),
]
