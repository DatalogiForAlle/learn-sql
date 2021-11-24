from django.db import models


class City(models.Model):
    name = models.CharField(max_length=50)
    size = models.IntegerField()

    class Meta:
        db_table = 'city'

    def __str__(self):
        return self.name


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    age = models.IntegerField()
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.first_name
