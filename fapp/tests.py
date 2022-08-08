from django.test import TestCase

# Create your tests here.
from .models import*
admin.site.register()
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(BookInstance)