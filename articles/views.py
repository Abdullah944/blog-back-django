from .forms import ArticleForm
from django.shortcuts import render, redirect
from .forms import ModelNameForm
from .models import Article
from .forms import UserRegister
from .forms import UserLogin
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from django.http import Http404
from django.db.models import Q


# from django.http import HttpResponse

# ? CONTROLLERS:
# ?views.py controls the flow of data in our app.
# Create your views here.

# not used

# def hello(request):
# return HttpResponse("<h1> Hello</h1>")

# ? HOME page:
def home(request):
    context = {
        "title": "Home",
        "header": "Welcome to our site!",
    }
    return render(request, "home_page.html", context)


# ? detail page:
def article_detail(request, article_id):
    context = {
        "article": Article.objects.get(id=article_id),
    }
    return render(request, "article_detail_page.html", context)


# ? get list + search
def article_list(request):
    articles = Article.objects.all()

    query = request.GET.get("q")
    if query:
        articles = articles.filter(
            Q(title__icontains=query)
            | Q(content__icontains=query)
            | Q(author__username__icontains=query)
        ).distinct()

    context = {
        "articles": articles,
    }
    return render(request, "article_list.html", context)


# ? create view || page:
def create_view(request):
    form = ModelNameForm()
    if request.method == "POST":
        form = ModelNameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list-view")
    context = {"form": form}
    return render(request, "create_page.html", context)


# ? update  controls:
def article_update(request, article_id):
    article = Article.objects.get(id=article_id)
    form = ArticleForm(instance=article)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect("article-list")
    context = {"article": article, "form": form}
    return render(request, "article_update.html", context)


# ? Auth Controllers:
def user_register(request):
    form = UserRegister()
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            user.set_password(user.password)
            user.save()

            login(request, user)
            # Where you want to go after a successful signup
            return redirect("successful-signup")
    context = {
        "form": form,
    }
    return render(request, "register.html", context)


def user_login(request):
    form = UserLogin()
    if request.method == "POST":
        form = UserLogin(request.POST)
        if form.is_valid():

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                # Where you want to go after a successful login
                return redirect("successful-login")

    context = {"form": form}
    return render(request, "login.html", context)


def logout_view(request):
    logout(request)
    return redirect("success-page")


# ? 404 Controller:
def not_found(request):
    if not request.user.is_staff:
        raise Http404
