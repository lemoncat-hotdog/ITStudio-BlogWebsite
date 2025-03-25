from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required(login_url='user:login')
def homepage_view(request):
    return render(request, "Hub.html")