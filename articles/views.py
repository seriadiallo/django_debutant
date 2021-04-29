from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from .forms import ArticleForm
from .models import Article




def malist(request):

    template_name = 'articles/list.html'
    clients = [
        {'nom': 'diallo', 'prenom': 'mamadou', 'age': 34, 'adresse': 'coyah'},
        {'nom': 'sow', 'prenom': 'Oumarou', 'age': 34, 'adresse': 'coza'},
        {'nom': 'Barry', 'prenom': 'Kadiatou', 'age': 24, 'adresse': 'Koloma'},
        {'nom': 'diallo', 'prenom': 'Mariame', 'age': 21, 'adresse': 'Bambeto'},
    ]
    context = {'clients': clients}

    return render(request, template_name, context)



def home(request):
    context = {}
    template_name = 'articles/home.html'

    return render(request, template_name, context)




def index(request):

    template_name = 'articles/index.html'
    ar = Article.objects.all()
    context = {
        'articles': ar
    }
    return render(request, template_name, context)


def create(request):

    template_name = 'articles/create.html'
    if request.method == "GET":
        form = ArticleForm()
        context = {
            'form': form
        }
        return render(request, template_name, context)

    elif request.method == 'POST':
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("articles:index", permanent=True)
        else:
            context = {
                'form': form
            }
            return render(request, template_name, context)


def detail(request, id):

    article = Article.objects.get(id=id)
    context = {
        'article': article
    }
    template_name = 'articles/detail.html'
    return render(request, template_name, context)


class ArticleDeleteView(DeleteView):
    model = Article
    pk_url_kwarg = 'id'
    template_name_suffix = '_delete_confirm'
    success_url = reverse_lazy('articles:index')

    