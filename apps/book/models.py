from django.db import models


from django.db import models
from apps.base.models import BaseModel
from simple_history.models import HistoricalRecords

class Author(BaseModel):
    last_name = models.CharField('last_name', max_length=50, null=True, blank=False)
    first_name = models.CharField('first_name', max_length=50, null=True, blank=False)
    # fecha_nacimiento = models.DateField('Fecha Nacimiento', blank=True, null=False)
    historical = HistoricalRecords()

    @property
    def _history_author(self):
        return self.change_by

    @_history_author.setter
    def _history_author(self, value):
        self.change_by = value

    class Meta:
        verbose_name = 'author'
        verbose_name_plural = 'authors'

    def __str__(self):
        return f'{self.last_name} {self.first_name}'


class Author(BaseModel):
    last_name = models.CharField('last_name', max_length=50, null=True, blank=False)
    first_name = models.CharField('first_name', max_length=50, null=True, blank=False)
    historical = HistoricalRecords()

    @property
    def _history_author(self):
        return self.change_by

    @_history_author.setter
    def _history_author(self, value):
        self.change_by = value

    class Meta:
        verbose_name = 'author'
        verbose_name_plural = 'authors'

    def __str__(self):
        return f'{self.last_name} {self.first_name}'


class Category(BaseModel):
    name = models.CharField('name', max_length=50, null=False, blank=False)
    recommended_age = models.CharField('recommended_age', max_length=50, null=False, blank=False)
    historical = HistoricalRecords()

    @property
    def _history_category(self):
        return self.change_by

    @_history_category.setter
    def _history_category(self, value):
        self.change_by = value

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categorys'

    def __str__(self):
        return f'{self.name}'


class Partner(BaseModel):
    last_name = models.CharField('Last_name', max_length=50, null=False, blank=False)
    first_name = models.CharField('Name', max_length=50, null=False, blank=False)
    dni = models.CharField('dni', max_length=50, blank=True, null=False)
    historical = HistoricalRecords()

    @property
    def _history_partner(self):
        return self.change_by

    @_history_partner.setter
    def _history_partner(self, value):
        self.change_by = value

    class Meta:
        verbose_name = 'partner'
        verbose_name_plural = 'partners'

    def __str__(self):
        return f'{self.last_name} {self.first_name}'



class Bookloan(BaseModel):
    status = models.CharField('Status', max_length=50, null=True, blank=False)
    book = models.ForeignKey('Book', on_delete=models.CASCADE, null=True, blank=True,  verbose_name="book")
    partner = models.ForeignKey('Partner',  on_delete=models.CASCADE, null=True, blank=False, verbose_name="Partner")
    historical = HistoricalRecords()

    @property
    def _history_bookloan(self):
        return self.change_by

    @_history_bookloan.setter
    def _history_bookloan(self, value):
        self.change_by = value

    class Meta:
        verbose_name = 'bookloan'
        verbose_name_plural = 'bookloans'

    def __str__(self):
        return f'{self.status}'


class Book(BaseModel):
    # last_name = models.CharField('Last_name', max_length=50, null=False, blank=False)
    name = models.CharField('Name', max_length=50, null=True, blank=False)
    isbn = models.CharField('isbn', max_length=50, blank=True, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, verbose_name='category')
    author = models.ForeignKey(Author, on_delete=models.CASCADE,  verbose_name='author', null=True)
    historical = HistoricalRecords()

    @property
    def _history_book(self):
        return self.change_by

    @_history_book.setter
    def _history_book(self, value):
        self.change_by = value

    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'books'

    def __str__(self):
        return f'{self.name}'