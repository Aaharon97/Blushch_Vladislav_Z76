from django.db import models


class Model1(models.Model):
    Part = models.TextField(max_length=100)
    Cat = models.CharField(max_length=100)


class Model2(models.Model):
    Catnumb = models.ForeignKey(Model1, on_delete=models.CASCADE)
    Cat_name = models.TextField()
    Price = models.CharField(max_length=100)


