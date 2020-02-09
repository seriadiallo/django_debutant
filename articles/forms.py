from django import forms

from .models import Article

class ArticleForm(forms.ModelForm):

    # titre = forms.CharField(max_length=30)
    # description = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, "cols": 20}))
    # date_pub = forms.DateField()
    # auteur = forms.CharField(max_length=50)

    class Meta:

        model = Article
        fields = ('titre', 'description', 'date_pub', 'auteur')