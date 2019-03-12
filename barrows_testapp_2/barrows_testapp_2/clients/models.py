from django.db import models

class Client(models.Model):
    client_name = models.CharField(max_length=50)
    contact_person = models.CharField(max_length=50)
    contact_no = models.IntegerField(blank=True, null=True)