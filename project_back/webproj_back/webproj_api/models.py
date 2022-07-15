from tkinter import CASCADE
from django.db import models

# Create your models here.

class Game(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Game'
        verbose_name_plural = 'Games'
        ordering = ('name',)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
        }

class GameImages(models.Model):
    game_id = models.ForeignKey(Game, on_delete=CASCADE)
    thumbnail = models.TextField(max_length=2047)
    background_img = models.TextField(max_length=2047)
    screenshot1 = models.TextField(max_length=2047)
    screenshot2 = models.TextField(max_length=2047)
    screenshot3 = models.TextField(max_length=2047)
    screenshot4 = models.TextField(max_length=2047)

    class Meta:
        verbose_name = 'Game Images'
        verbose_name_plural = 'Game Images'

    def to_json(self):
        return {
            'id': self.game_id,
            'thumbnail': self.thumbnail,
            'background_img': self.background_img,
            'screenshot1': self.screenshot1,
            'screenshot2': self.screenshot2,
            'screenshot3': self.screenshot3,
            'screenshot4': self.screenshot4,
        }


class GameDescription(models.Model):
    game_id = models.ForeignKey(Game, on_delete=CASCADE)
    description = models.TextField(max_length=2047)
    website_url = models.TextField(max_length=2047)
    publisher = models.CharField(max_length=255)
    platforms = models.CharField(max_length=255)
    likes = models.IntegerField()
    dislikes = models.IntegerField()

    class Meta:
        verbose_name = 'Game Description'
        verbose_name_plural = 'Game Description'


    def to_json(self):
        return {
            'id': self.game_id,
            'description': self.description,
            'website_url': self.website_url,
            'publisher': self.publisher,
            'platforms': self.platforms,
            'likes': self.likes,
            'dislikes': self.dislikes,
        }


class GameDetails(models.Model):
    game_id = models.ForeignKey(Game, on_delete=CASCADE)
    release_date = models.CharField(max_length=255)
    genres = models.CharField(max_length=255)
    metacritic_points = models.IntegerField()

    class Meta:
        verbose_name = 'Game Details'
        verbose_name_plural = 'Game Details'

    def to_json(self):
        return {
            'id': self.game_id,
            'release_date': self.release_date,
            'genres': self.genres,
            'metacritic_points': self.metacritic_points,
        }





