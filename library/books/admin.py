from .models import Book
from django.contrib import admin

# Register your models here.


@admin.register(Book)
class Admin(admin.ModelAdmin):
    """
    Класс Admin предоставляет настройки для отображения и функционирования модели Book в админ панели Django.

    Атрибуты:
        list_display (tuple[str, ...]): какие поля модели будут отображаться в админ панели
        list_filter (tuple[str, ...]): по каким полям модели будет доступна фильтрация записей
        search_fields (tuple[str, ...]): по каким полям модели будет производиться поиск по записям
    """
    list_display: tuple[str, ...] = ('title', 'author', 'status', 'renter_name',
                                     'rent_date', 'return_date', 'is_overdue', 'penalty')
    list_filter: tuple[str, ...] = ('renter_name', 'author', 'rent_date')
    search_fields: tuple[str, ...] = ('title', 'author', 'renter_name')
