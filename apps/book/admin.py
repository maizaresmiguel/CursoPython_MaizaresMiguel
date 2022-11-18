from django.contrib import admin
from apps.book.models import *
# Register your models here.
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Partner)
admin.site.register(Bookloan)

