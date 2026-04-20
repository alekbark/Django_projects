from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Child(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    favorite_icecream = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class IceCream(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Kiosk(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name