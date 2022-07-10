from django.urls import path
from djbooks import views
from djbooks.views import Link

urlpatterns = [
    path("", views.home, name="home"),
    path("publisher/<pub_id>", views.publisher, name="publisher"),
    path("book/<book_id>", views.book, name='book'),
    path("books", views.book_list, name='books'),
    path("authors", views.author_list, name='authors'),
    path("new-publisher", views.get_publisher, name='new-publisher'),
    path("new-author", views.get_author, name='new-author'),
    path("links", Link.as_view(), name='links')
]
