from django.db import models

# Create your models here.

class Todo(models.Model):
    """
    basic structure of to-dos
    """
    title = models.CharField(max_length=100)
    body = models.TextField()
    
    def __str__(self):
        return self.title
        