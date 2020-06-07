from django.http import HttpResponse
from django.shortcuts import render,redirect 
from .forms import ContactForm,LoginForm,RegisterForm
from django.contrib.auth import authenticate , login , get_user_model

def home_page(request):
    context = {
        "title" : "Hello World",
        "content" : "Wellcome to the homepage"
    }
    if request.user.is_authenticated:
        context["premium_content"] = "YEAHHHHHHH"
    return render(request,"home_page.html",context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
         "title" : "Contact",
         "content":"Welcome to Contact Page",
         "form":contact_form ,
         "brand" : "brand form"
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    # if request.method == "POST":
    #     print(request.POST.get("fullname"))
    #     print(request.POST.get("email"))
    #     print(request.POST.get("content"))
    return render(request,"contact/view.html",context)