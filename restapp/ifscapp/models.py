from django.db import models

# created a Model to contain the dataset variables

from django.db import models

class Bankdata(models.Model):
    IFSC = models.CharField(max_length=11)
    Bank_id = models.CharField(max_length=10)
    Branch = models.CharField(max_length=50)
    Address = models.CharField(max_length=300)
    City = models.CharField(max_length=50)
    District = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    BankName = models.CharField(max_length=100)

    def __str__(self):
        return self.Branch #returned the Branch name for model