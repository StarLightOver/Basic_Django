from django.db import models


class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        """Отвечает за то, как объект будет выводит на html-странице"""
        return self.title

    def get_absolute_url(self):
        """Отвечает за получение абсолютного url"""
        return f"/news/{self.id}"

    class Meta:
        """Мета-параметры модели"""
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
