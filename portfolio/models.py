from django.db import models

class Project(models.Model):
    title=models.CharField(max_length=100) # ограничивает количество символов в заголовке
    description=models.CharField(max_length=300) # ограничивает количество символов в описании
    image=models.ImageField(upload_to='portfolio/images/') # создает папку, где будут храниться медиафайлы
    url=models.URLField(blank=True) #Открытие ссылки на новой вкладке

    def __str__(self):
        return self.title
