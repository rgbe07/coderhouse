from django.db import models

class Family(models.Model):
    name = models.CharField(max_length=40)
    ages = models.IntegerField()
    birth = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} | {self.ages} | {self.birth}"
