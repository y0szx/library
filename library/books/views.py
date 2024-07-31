from .models import Book
from typing import Union
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def book_list(request: HttpRequest) -> HttpResponse:
    """
    Формирует список книг для отображения с возможностью сортировки по полям.

    Args:
        request (HttpRequest): запрос с данными

    Returns:
        HttpResponse: рендер шаблона books/book_list.html с контекстом со списком книг
    """
    order_by: str = request.GET.get('order_by', 'title')
    direction: str = request.GET.get('direction', 'asc')

    books: list[Book] = list(Book.objects.all())

    if order_by in ['is_overdue', 'penalty']:
        if order_by == 'is_overdue':
            books.sort(key=lambda x: x.is_overdue(),
                       reverse=(direction == 'desc'))
        elif order_by == 'penalty':
            books.sort(key=lambda x: x.penalty(),
                       reverse=(direction == 'desc'))
    else:
        if direction == 'desc':
            order_by = f'-{order_by}'
        books = Book.objects.all().order_by(order_by)

    context: dict[str, Union[Book, str]] = {
        'books': books,
        'order_by': order_by,
        'direction': direction
    }

    return render(request, 'books/book_list.html', context)
