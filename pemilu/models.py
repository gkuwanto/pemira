from django.db import models

# Create your models here.
class Password(models.Model):
    password = models.CharField(max_length=50)
    current = models.BooleanField()
    def __str__(self):
        if self.current:
            return f"{self.password} - current"
        else:
            return self.password

class Candidate(models.Model):
    no = models.IntegerField()
    name = models.CharField(max_length=255)
    year = models.IntegerField()
    current = models.BooleanField()
    def __str__(self):
        return f"{self.year} - {self.name} / {self.no}"

class Vote(models.Model):
    year = models.IntegerField()
    no = models.IntegerField()
    def __str(self):
        return f"{self.year} {self.no}"
