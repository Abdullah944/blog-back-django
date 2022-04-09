from django import forms
from .models import Article
from django.db import models
from django.contrib.auth.models import User

# Create your models here #?(SCEHMA).
# ?models.py is how we map our data to the database.


class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=120)
    pic = models.ImageField()  # add image

    def __str__(self):
        return self.title


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "content", "author"]


class UserRegister(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password"]

        widgets = {
            "password": forms.PasswordInput(),
        }


# one to many
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
