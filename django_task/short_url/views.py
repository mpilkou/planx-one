from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
# @login_required()
# def index(req):
#     return render(req, 'index.html')

class UrlView(LoginRequiredMixin, View):

    def get(self, req):
        return render(req, 'index.html')
    
    def post(self, req):
        pass