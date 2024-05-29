from django.db import models


class Tech(models.Model):
    name = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to="about/techs")
    def __str__(self):
        return self.name

class Certification(models.Model):
    name = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to="about/certs")
    def __str__(self):
        return self.name