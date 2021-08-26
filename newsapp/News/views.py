from django.http import  JsonResponse
from django.conf import settings
import requests
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from .models import Article
from django.shortcuts import render, redirect, get_object_or_404

temp_img = "https://images.pexels.com/photos/3225524/pexels-photo-3225524.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500"


def home(request):
    page = request.GET.get('page', 1)
    search = request.GET.get('search', None)

    #Search for top news arround the world using NewsAPI
    if search is None or search=="top":
        url = "https://newsapi.org/v2/top-headlines?country={}&page={}&apiKey={}".format(
            "us",1,settings.APIKEY
        )
    else:
        #Search for queries
        url = "https://newsapi.org/v2/everything?q={}&sortBy={}&page={}&apiKey={}".format(
            search,"popularity",page,settings.APIKEY
        )

    #Get articles urls
    r = requests.get(url=url)

    #data as json
    data = r.json()
    if data["status"] != "ok":
        return HttpResponse("<h1>Request Failed</h1>")

    #data as array
    data = data["articles"]
    context = {
        "success": True,
        "data": [],
        "search": search
    }

    # Serparate the requested data
    for i in data:
        context["data"].append({
            "title": i["title"],
            "description":  "" if i["description"] is None else i["description"],
            "url": i["url"],
            "image": temp_img if i["urlToImage"] is None else i["urlToImage"],
            "publishedat": i["publishedAt"]

        })
    # send the data to home page
    return render(request, 'index.html', context=context)


def loadcontent(request):
    try:
        page = request.GET.get('page', 1)
        search = request.GET.get('search', None)
        url = "https://newsapi.org/v2/everything?q={}&sortBy={}&page={}&apiKey={}".format(
            "Technology","popularity",page,settings.APIKEY
        )
        if search is None or search=="top":
            url = "https://newsapi.org/v2/top-headlines?country={}&page={}&apiKey={}".format(
                "us",page,settings.APIKEY
            )
        else:
            url = "https://newsapi.org/v2/everything?q={}&sortBy={}&page={}&apiKey={}".format(
                search,"popularity",page,settings.APIKEY
            )
        print("url:",url)
        r = requests.get(url=url)

        data = r.json()
        if data["status"] != "ok":
            return JsonResponse({"success":False})
        data = data["articles"]
        context = {
            "success": True,
            "data": [],
            "search": search,

        }
        for i in data:

            context["data"].append({
                "title": i["title"],
                "description":  "" if i["description"] is None else i["description"],
                "url": i["url"],
                "image": temp_img if i["urlToImage"] is None else i["urlToImage"],
                "publishedat": i["publishedAt"]

            })

        return JsonResponse(context)
    except Exception as e:
        return JsonResponse({"success":False})

#Regisration Method
def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Registration successful.")
            login(request, user)
            return redirect("Home")
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")

    form = NewUserForm()
    return render (request=request, template_name="register.html", context={"register_form":form})


#Login Method
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password,email=email)

            if user is not None:
                login(request, user)
                messages.success(request, f"You are now logged in as {username}.")
                return redirect('Home')
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form":form})

#Logout Method
def logout_request(request):

    logout(request)
    messages.warning(request, "You have successfully logged out.")
    return redirect("Home")

#Save articles to DB
def storea_rticles(request):
    page = request.GET.get('article', 1)
    search = request.GET.get('search', None)
    if search is None or search=="top":
        # get the top news
        url = "https://newsapi.org/v2/top-headlines?country={}&page={}&apiKey={}".format(
            "us",1,settings.APIKEY
        )
    else:
        url = "https://newsapi.org/v2/everything?q={}&sortBy={}&page={}&apiKey={}".format(
            search,"popularity",page,settings.APIKEY
        )
    r = requests.get(url=url)
    data = r.json()
    data=data["articles"]
    for i in data:
        title=i["title"]
        url=i["url"]
        description=i["description"]
        art_fav=Article.objects.create(title=title,url=url,description=description)
        art_fav.save()
    messages.success(request, "You saved the articles to the database!")
    return redirect("Home")

def artdb(request):
    data = Article.objects.all()

    art = {
        "art_id":data

    }
    return render(request, "artdb.html", context=art)

def bookmark(request):
    data = Article.objects.all()
