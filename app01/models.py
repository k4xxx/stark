import win_unicode_console
win_unicode_console.enable()

from django.db import models

class Author(models.Model):
    name = models.CharField(verbose_name='姓名',max_length=32)
    age = models.IntegerField(verbose_name='年纪')
    sex = models.CharField(verbose_name='性别',max_length=8)

    def __str__(self):
        return self.name



class Book(models.Model):
    title = models.CharField(verbose_name='名称',max_length=32)
    author = models.ForeignKey(verbose_name='作者',to='Author')
    publish = models.ManyToManyField(verbose_name='出版社',to='Publish')

    def __str__(self):
        return self.title


class Publish(models.Model):
    title = models.CharField(max_length=32)

    def __str__(self):
        return self.title