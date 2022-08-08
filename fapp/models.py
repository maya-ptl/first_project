from tkinter import CASCADE
from django.db import models

# Create your models here.
class Student(models.Model):
    student_name=models.CharField(max_length=40)
    def __str__(self):
        return self.student_name

class Teacher(models.Model):
    Teacher_name=models.CharField(max_length=40)
    Student=models.ForeignKey(Student,on_delete=models.CASCADE, null =True, blank = True,related_name='student') 

    def __str__(self):
        return self.Teacher_name



class Artical(models.Model):
    topic=models.CharField(max_length=40)
    def __str__(self):
        return self.topic

class Application(models.Model):
    apliction_name=models.CharField(max_length=40)
    tap=models.ManyToManyField(Artical)
   
    def __str__(self):
        return self.apliction_name

class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
    shirt_price=models.DecimalField(verbose_name='price', max_digits=4, decimal_places=2,null=True,blank=True)
    def __str__(self):
        return self.name

    
class Artist(models.Model):
    name = models.CharField(max_length=10)

class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.RESTRICT)


class User(models.Model):
    user_name=models.CharField(verbose_name='user',max_length=40)

class Page(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)




class Commoninfo(models.Model):
    age=models.BigIntegerField()
    date=models.DateField()
    firstname=models.CharField(max_length=40)
    lastname=models.CharField(max_length=40)
    
    class Meta:
        abstract=True

class Children(Commoninfo):
    fees=models.IntegerField()

class Tutor(Commoninfo):
    salary=models.FloatField()





