from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.contrib import auth
from django.template import RequestContext

from .forms import MyUserCreationForm,EtudiantForm
# Create your views here.

def subscribe(request):
    pass

def logout(request):
    auth.logout(request)
    return render(request, 'home.html')

def home(request):

    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        uf = MyUserCreationForm(request.POST, prefix='user')
        upf = EtudiantForm(request.POST, prefix='userprofile')
        if uf.is_valid() * upf.is_valid():
            user = uf.save()
            userprofile = upf.save(commit=False)
            userprofile.user = user
            userprofile.save()
            return HttpResponseRedirect("/accounts/profile")
    else:
        uf = MyUserCreationForm(prefix='user')
        upf = EtudiantForm(prefix='userprofile')
        context = dict(userform=uf,userprofileform=upf)
    return render(request,'register_etudiant.html',context)