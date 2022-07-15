from django.contrib import admin
from .models import Game, GameImages, GameDescription, GameDetails

# Register your models here.
admin.site.register(Game)
admin.site.register(GameImages)
admin.site.register(GameDescription)
admin.site.register(GameDetails)


