from django.db import models


class Customer(models.Model):
    #customerNumber = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=50)
    contact_last_name = models.CharField(max_length=50)
    contact_first_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    class Meta:
        # Change default name of table from 'learnsql_customer' to 'customer'
        db_table = 'customer'

    def __str__(self):
        return self.customer_name
