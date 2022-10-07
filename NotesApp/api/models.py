from django.db import models

# Create your models here.


class Note(models.Model):
    body = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'notes'
    
    def __str__(self):
        return self.body