from django.db import models

class ModelFile(models.Model):
    image = models.ImageField('画像', upload_to='documents/')
    label = models.CharField('推論結果', blank=True, null=True, max_length=30)
    proba = models.FloatField('信頼度', default=0.0)

def __str__(self):
    return self.title