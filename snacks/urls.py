from django.urls import path
from .views import HomePageView, AboutPageView


# setting path so when traffic is directed from project to application, I want you to display the home page view
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about', AboutPageView.as_view(), name='about'),
]
