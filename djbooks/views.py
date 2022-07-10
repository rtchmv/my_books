from unicodedata import name
from unittest import result
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Author, Book, Publisher, UsersLink
from django.http import HttpResponseRedirect
from .forms import PublisherForm, AuthorForm, UsersLinkForm
from django.urls import reverse
from django.views import View


def home(request):
    publisher_queryset = Publisher.objects.all()
    if 'msg' in request.session.keys():
        msg = request.session['msg']
        request.session['msg'] = ''
    else:
        msg = ''
    return render(request, 'djbooks/home.html', {'publisher_queryset': publisher_queryset, 'msg': msg})


def publisher(request, pub_id):
    pub_inf = Publisher.objects.get(id=pub_id)
    return render(request, 'djbooks/publisher.html', {'pub_inf': pub_inf})


def book(request, book_id):
    book_queryset = Book.objects.get(id=book_id)
    return render(request, 'djbooks/book.html', {'book_query': book_queryset})


def book_list(request):
    book_queryset = Book.objects.order_by('title')
    return render(request, 'djbooks/books.html', {'book_queryset': book_queryset})


def author_list(request):
    authors_queryset = Author.objects.order_by('name')
    if 'msg' in request.session.keys():
        msg = request.session['msg']
        request.session['msg'] = ''
    else:
        msg = ''
    return render(request, 'djbooks/authors.html', {'authors_queryset': authors_queryset, 'msg': msg})


def get_publisher(request):
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            publisher = Publisher(name=form.cleaned_data['name'], address=form.cleaned_data['address'], city=form.cleaned_data['city'],
                                  country=form.cleaned_data['country'], website=form.cleaned_data['website'])  # тут ошибка была - не cleaned_data.name, а cleaned_data['name']
            publisher.save()
            request.session['msg'] = f"New publisher {form.cleaned_data['name']} has been added. Congratulations!"
            return redirect("home")
    else:
        form = PublisherForm()

    # тут ошибка - в адресе не было djbooks/
    return render(request, 'djbooks/addpublisher.html', {'form': form})


def get_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            request.session['msg'] = f"New author {form.cleaned_data['salutation']} {form.cleaned_data['name']} has been added."
            return redirect('authors')
    else:
        form = AuthorForm()

    return render(request, 'djbooks/addauthor.html', {'form': form})

class Link(View):
    template_name = 'djbooks/links.html'
    initial = {'links': 'http://'}
    form_class = UsersLinkForm
     
    #def links(self, request):
    #    links_queryset = UsersLink.objects.all()
    #    return render(request, self.template_name, {'links_queryset': links_queryset})

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        links_queryset = UsersLink.objects.order_by('-pk')
        return render(request, self.template_name, {'form': form, 'links_queryset' : links_queryset})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('links')
        else:
            form = self.form_class()
        return render(request, self.template_name, {'form': form})



