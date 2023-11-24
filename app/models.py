from django.db import models


class emailsent(models.Model):
    name = models.CharField(max_length=255,default='')
    email = models.CharField(max_length=255)

class mailing(models.Model):
    name = models.CharField(max_length=255,default='')
    email = models.CharField(max_length=255)


class newemail(models.Model):
    name = models.CharField(max_length=255,default='')
    email = models.CharField(max_length=255)
    
   



