from django.http import HttpResponseNotFound
from django.shortcuts import redirect, render
from django.views import View

from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.core.exceptions import ValidationError, ObjectDoesNotExist


from short_url_app.models import URL

class UrlView(LoginRequiredMixin, View):

    def get(self, req):
        return render(req, 'index.html')
    
    def post(self, req):
        error = None
        url = req.POST.get('url')
        url_model = URL(sourse_url = url, user = req.user)
        try:
            print(url_model.clean_fields())
        except ValidationError:
            error = 'Your URL is not valid'
            return render(req, 'index.html', {'error':f'{error}'})
        else:
            url_model.save()
        new_url = f'{ "http://" + req.get_host() + "/" + url_model.short_url}'
        return render(req, 'index.html', {'generated_url':f'{new_url}'})

class GeneratedUrlView(View):
    def get(self, req, short_url):
        redirect_url = URL.objects.filter(short_url = short_url)
        if len(redirect_url) == 0:
            return HttpResponseNotFound("Страница не найдена")
        
        return redirect(redirect_url.first().sourse_url)

class SignUp(View):
    def get(self, req):
        return render(req, 'registration/signup.html')

    def post(self, req):
        user = None
        username=req.POST.get('username')
        password=req.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except ObjectDoesNotExist:
            '''expected error (user not exist)'''
            pass
        else:
            return render(req, 'registration/signup.html', {'error':'user already exists'})
        
        user = User(username = username, password = password)
        user.set_password(user.password)
        user.save()

        user = authenticate(req, username=username, password=password)
        login(req, user)
        print(user)
        return redirect('/')
