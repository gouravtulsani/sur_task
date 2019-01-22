from django.db import models

class AdultData(models.Model):
    age = models.IntegerField()
    work_class = models.CharField(max_length=50, null=True)
    fnlwgt = models.BigIntegerField()
    education = models.CharField(max_length=50)
    ed_no = models.IntegerField()
    marital_status = models.CharField(max_length=50)
    occupation = models.CharField(max_length=50, null=True)
    relationship = models.CharField(max_length=50, db_index=True)
    race = models.CharField(max_length=50, db_index=True)
    sex = models.CharField(max_length=50, db_index=True)
    capital_gain = models.IntegerField()
    capital_loss = models.IntegerField()
    hours_per_week = models.IntegerField()
    native_country = models.CharField(max_length=50, null=True)
    income_range = models.CharField(max_length=10)


