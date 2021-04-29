from django import forms

from .models import Article

class ArticleForm(forms.ModelForm):

    # Personnaliser les champs 'description' et 'date_pub'
    description = forms.CharField(widget=forms.TextInput(attrs={'rows': 100, "cols": 20, 'class': 'materialize-textarea'}))
    date_pub = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class': 'datepicker', 'type': 'text'}), 
            input_formats=['%Y-%m-%d',      # '2006-10-25'
                '%m/%d/%Y',      # '10/25/2006'
 '              %m/%d/%y',      # '10/25/06'
                '%b %d %Y',      # 'Oct 25 2006'
                '%b %d, %Y',     # 'Oct 25, 2006'
                '%d %b %Y',      # '25 Oct 2006'
                '%d %b, %Y',     # '25 Oct, 2006'
                '%B %d %Y',      # 'October 25 2006'
                '%B %d, %Y',     # 'October 25, 2006'
                '%d %B %Y',      # '25 October 2006'
                '%d %B, %Y',     # '25 October, 2006'
                '%Y-%m-%d %H:%M:%S',    # '2006-10-25 14:30:59'
                '%Y-%m-%d %H:%M',       # '2006-10-25 14:30'
                '%m/%d/%Y %H:%M:%S',    # '10/25/2006 14:30:59'
                '%m/%d/%Y %H:%M',       # '10/25/2006 14:30'
                '%m/%d/%y %H:%M:%S',    # '10/25/06 14:30:59'
                '%m/%d/%y %H:%M',]       # '10/25/06 14:30'
    )

    class Meta:

        model = Article
        fields = ('titre', 'description', 'date_pub', 'auteur')