from django.db import models

class ModelFile(models.Model):
    image = models.ImageField('画像', upload_to='documents/')

def __str__(self):
    return self.title