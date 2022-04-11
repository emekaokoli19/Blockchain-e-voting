from django.db import models

class Voter(models.Model):
    name = models.CharField(max_length=200)
    PVC_no = models.CharField(max_length=10)
    password = models.CharField(max_length=25)
    vote_ID = models.CharField(max_length=20)
    vote_status = models.BooleanField()

    def __str__(self) -> str:
        return self.vote_ID