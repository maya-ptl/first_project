from django.contrib import admin

# Register your models here.
from .models import Student,Teacher
admin.site.register(Student)
admin.site.register(Teacher)
from .models import Artical,Application,Person,Artist,Album,Song,User,Page,Children,Tutor
admin.site.register(Artical)
admin.site.register(Application)
admin.site.register(Person)
admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Song)
admin.site.register(User)
admin.site.register(Page)
admin.site.register(Children)
admin.site.register(Tutor)

