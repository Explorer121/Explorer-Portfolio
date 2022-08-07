from django.shortcuts import render

# Create your views here.
def login_attempt(request):
     
	context = {}
	return render(request, "login.html", context)

def register_attempt(request):
	context = {}
	return render(request, "register.html", context)


def success(request):
     context = {}
     return render(request, "success.html", context)
	

def token_send(request):
	context = {}
	return render(request, "token_send.html", context)

