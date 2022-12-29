from django.urls import path
from .views import DrinksHomePageView, DrinksAboutPageView


# setting path so when traffic is directed from project to application, I want you to display the home page view
urlpatterns = [
    path('', DrinksHomePageView.as_view(), name='home_drinks'),
    path('about', DrinksAboutPageView.as_view(), name='about_drinks'),
]
