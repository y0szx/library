from django.db import models
from django.utils import timezone

# Create your models here.


class Book(models.Model):
    """
    Класс Book описывает модель книги в системе.

    Атрибуты:
        STATUS (list[tuple[str, str]]): список кортежей с возможными статусами книги
        title (str): название книги
        author (str): автор книги
        status (str): статус книги
        renter_name (str): имя арендатора книги, если книга находится в аренде
        rent_date (models.DateField): дата взятия в аренду
        return_date (models.DateField): дата, когда нужно вернуть книгу
    """
    STATUS: list[tuple[str, str]] = [
        ('available', 'В библиотеке'),
        ('rented', 'В аренде'),
    ]

    title: str = models.CharField(max_length=100)
    author: str = models.CharField(max_length=100)
    status: str = models.CharField(
        max_length=10, choices=STATUS, default='available')
    renter_name: str = models.CharField(max_length=100, blank=True, null=True)
    rent_date: models.DateField = models.DateField(blank=True, null=True)
    return_date: models.DateField = models.DateField(blank=True, null=True)

    def is_overdue(self) -> bool:
        """
        Определяет, просрочена ли аренда книги

        Returns:
            bool: просрочена или нет
        """
        if self.status == 'rented' and self.return_date:
            return self.return_date < timezone.now().date()
        return False

    def days_overdue(self) -> int:
        """
        Определяет на сколько дней была просрочена аренда книги

        Returns:
            int: кол-во дней
        """
        if self.is_overdue():
            return (timezone.now().date() - self.return_date).days
        return 0

    def penalty(self) -> int:
        """
        Считает сумму штрафа за просроченную аренду книги

        Returns:
            int: сумма штрафа
        """
        penalty = 100
        return self.days_overdue() * penalty

    def __str__(self) -> str:
        """
        Возвращает строковое представлений объекта Book

        Returns:
            str: строковое представление объекта Book
        """
        return f'{self.title} by {self.author}'
