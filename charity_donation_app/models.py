from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Institution(models.Model):
    CHOICES = [
        ('fundacja', 'Fundacja'),
        ('organizacja pozarządowa', 'Organizacja pozarządowa'),
        ('zbiórka lokalna', 'Zbiórka lokalna')
    ]
    name = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(max_length=30, choices=CHOICES, default='fundacja')
    category = models.ManyToManyField(Category)

    def __str__(self):
        return f"{self.name} {self.description} {self.category}"

class Donation(models.Model):
    quantity = models.IntegerField(help_text='Podaj liczbę worków')
    category = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.institution.name}"