from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from api.home.Values_const import LOGING_URL
#constantes valores



# Create your views here.
@login_required(login_url=LOGING_URL)

def home_views(request):
    template_name= "index.html"
    
    return render(request,template_name)