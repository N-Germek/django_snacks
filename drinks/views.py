from django.views.generic import TemplateView


class DrinksHomePageView(TemplateView):
    template_name = 'home_drinks.html'


class DrinksAboutPageView(TemplateView):
    template_name = 'about_drinks.html'
