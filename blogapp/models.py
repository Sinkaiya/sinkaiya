from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.created_date = timezone.now()  # Раньше здесь было publish_date, но его же нет в атрибутах...
        self.save()

    def __str__(self):
        return self.title


# Здесь будет модель для теста Айзенка
# class Eysenck(models.Model):
#     firstname = models.CharField(max_length=255)
#     lastname = models.CharField(max_length=255)
#     surname = models.CharField(max_length=255)
#     age = models.IntegerField()
#     versy = models.IntegerField()
#     vert = models.CharField(max_length=255)
#     neurotism = models.IntegerField()
#     neurotic = models.CharField(max_length=255)
#     unfair = models.IntegerField()
#     fairman = models.CharField(max_length=255)
