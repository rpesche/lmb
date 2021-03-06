from django.views import View
from django.template.loader import get_template
from django.http import HttpResponse


class Index(View):

    def get(self, request):
        template = get_template('index.jinja')
        return HttpResponse(template.render())


class Menu(View):

    def post(self, request):
        template = get_template('menu/menu.login.php')
        return HttpResponse(template.render())
