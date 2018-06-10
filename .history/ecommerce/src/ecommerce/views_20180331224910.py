from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    context = {
        "title":"Hello World!",
        "content":"Welcome to the homepage."
    }
    return render(request, "home_page.html", context)

def about_page(request):
    context = {
        "title":"About",
        "content":"Welcome to the about page."
    }
    return render(request, "home_page.html", context)

def contact_page(request):
    context = {
        "title":"Contact",
        "content":"Welcome to the contact page."
    }
    if request.method == "POST":
            print(request.POST)

    return render(request, "contact/view.html", context)