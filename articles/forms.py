from django import forms
from .models import Article


# ? ModelForm strucure:
# *Forms are always classes and the class Meta is used to create an association.
# * The association basically means, "hey this ModelForm is for this model!".
# *The fields list refer to the fields that your model has. The fields are included in the fields list which will be displayed when the form is rendered.

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'author']
