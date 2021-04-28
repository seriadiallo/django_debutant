from django import forms

from .models import Article

class ArticleForm(forms.ModelForm):

    # Personnaliser les champs 'description' et 'date_pub'
    description = forms.CharField(widget=forms.TextInput(attrs={'rows': 100, "cols": 20, 'class': 'materialize-textarea'}))
    date_pub = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker', 'type': 'text'}))

    class Meta:

        model = Article
        fields = ('titre', 'description', 'date_pub', 'auteur')