from django.db import models

class Blog(models.Model):
    title=models.CharField(max_length=200) # ограничивает количество символов в заголовке
    description=models.TextField() # ограничивает количество символов в описании
    date = models.DateField()
    def __str__(self):
        return self.title
