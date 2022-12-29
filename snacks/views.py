from django.views.generic import TemplateView


# this will create the home page view
class HomePageView(TemplateView):
    template_name = 'home.html'


# this will create the about page view
class AboutPageView(TemplateView):
    template_name = 'about.html'
