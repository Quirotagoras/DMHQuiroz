from django.views import generic

class RegisterDoctor(generic.TemplateView):
    template_name = '../templates/registerDoctor.html'


