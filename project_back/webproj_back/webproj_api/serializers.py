from dataclasses import fields
from rest_framework import serializers
from .models import Game, GameImages, GameDescription, GameDetails

# Create your serializers here

class GSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()

    def create(self, validated_data):
        game = Game.objects.create(name=validated_data['name'])
        return game

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        return instance


class GImgsSerializer(serializers.Serializer):
    game_id = serializers.IntegerField()
    thumbnail = serializers.CharField()
    background_img = serializers.CharField()
    screenshot1 = serializers.CharField()
    screenshot2 = serializers.CharField()
    screenshot3 = serializers.CharField()
    screenshot4 = serializers.CharField()


    def create(self, validated_data):
        game_images = GameImages.objects.create(
        thumbnail=validated_data['thumbnail'],
        background_img=validated_data['background_img'], 
        screenshot1=validated_data['screenshot1'],
        screenshot2=validated_data['screenshot2'],
        screenshot3=validated_data['screenshot3'],
        screenshot4=validated_data['screenshot4'])
        return game_images

    def update(self, instance, validated_data):
        instance.thumbnail = validated_data['thumbnail']
        instance.background_img = validated_data['background_img']
        instance.screenshot1 = validated_data['screenshot1']
        instance.screenshot2 = validated_data['screenshot2']
        instance.screenshot3 = validated_data['screenshot3']
        instance.screenshot4 = validated_data['screenshot4']
        return instance

class GDescSerializer(serializers.Serializer):
    game_id = serializers.IntegerField()
    description = serializers.CharField()
    website_url = serializers.CharField()
    publisher = serializers.CharField()
    platforms = serializers.CharField()
    likes = serializers.IntegerField()
    dislikes = serializers.IntegerField()

    def create(self, validated_data):
        game_description = GameImages.objects.create(
        description=validated_data['description'],
        website_url=validated_data['website_url'],
        publisher=validated_data['publisher'],
        platforms=validated_data['platforms'],
        likes=validated_data['likes'],
        dislikes=validated_data['dislikes'])
        return game_description

    def update(self, instance, validated_data):
        instance.description=validated_data['description']
        instance.website_url=validated_data['website_url']
        instance.publisher=validated_data['publisher']
        instance.platforms=validated_data['platforms']
        instance.likes=validated_data['likes']
        instance.dislikes=validated_data['dislikes']
        return instance


class GDetsSerializer(serializers.Serializer):
    game_id = serializers.IntegerField()
    release_date = serializers.CharField()
    genres = serializers.CharField()
    metacritic_points = serializers.IntegerField()

    def create(self, validated_data):
        game_details = GameImages.objects.create(
        release_date=validated_data['release_date'],
        genres=validated_data['genres'],
        metacritic_points=validated_data['metacritic_points'])
        return game_details

    def update(self, instance, validated_data):
        instance.release_date=validated_data['release_date']
        instance.genres=validated_data['genres']
        instance.metacritic_points=validated_data['metacritic_points']
        return instance

class AllSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    thumbnail = serializers.CharField()
    background_img = serializers.CharField()
    screenshot1 = serializers.CharField()
    screenshot2 = serializers.CharField()
    screenshot3 = serializers.CharField()
    screenshot4 = serializers.CharField()
    description = serializers.CharField()
    website_url = serializers.CharField()
    publisher = serializers.CharField()
    platforms = serializers.CharField()
    likes = serializers.IntegerField()
    dislikes = serializers.IntegerField()
    release_date = serializers.CharField()
    genres = serializers.CharField()
    metacritic_points = serializers.IntegerField()

    def create(self, validated_data):
        all = Game.objects.all().select_related('images', 'description', 'details').create(
            name=validated_data['name'],
            thumbnail=validated_data['thumbnail'],
            background_img=validated_data['background_img'], 
            screenshot1=validated_data['screenshot1'],
            screenshot2=validated_data['screenshot2'],
            screenshot3=validated_data['screenshot3'],
            screenshot4=validated_data['screenshot4'],
            description=validated_data['description'],
            website_url=validated_data['website_url'],
            publisher=validated_data['publisher'],
            platforms=validated_data['platforms'],
            likes=validated_data['likes'],
            dislikes=validated_data['dislikes'],
            release_date=validated_data['release_date'],
            genres=validated_data['genres'],
            metacritic_points=validated_data['metacritic_points'])
        return all

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.thumbnail = validated_data['thumbnail']
        instance.background_img = validated_data['background_img']
        instance.screenshot1 = validated_data['screenshot1']
        instance.screenshot2 = validated_data['screenshot2']
        instance.screenshot3 = validated_data['screenshot3']
        instance.screenshot4 = validated_data['screenshot4']
        instance.description=validated_data['description']
        instance.website_url=validated_data['website_url']
        instance.publisher=validated_data['publisher']
        instance.platforms=validated_data['platforms']
        instance.likes=validated_data['likes']
        instance.dislikes=validated_data['dislikes']
        instance.release_date=validated_data['release_date']
        instance.genres=validated_data['genres']
        instance.metacritic_points=validated_data['metacritic_points']
        return instance


class Game2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'name')


class GameImages2Serializer(serializers.ModelSerializer):
    class Meta:
        model = GameImages
        fields = ('game_id', 'thumbnail', 'background_img', 'screenshot1', 'screenshot2', 'screenshot3', 'screenshot4')

class GameDescription2Serializer(serializers.ModelSerializer):
    class Meta:
        model = GameDescription
        fields = ('game_id', 'description', 'website_url', 'publisher', 'platforms', 'likes', 'dislikes')


class GameDetails2Serializer(serializers.ModelSerializer):
    class Meta:
        model = GameDetails
        fields = ('game_id', 'release_date', 'genres', 'metacritic_points')

class All2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Game.objects.all().select_related('images', 'description', 'details')
        fields = (
        'id',
        'name',
        'thumbnail', 
        'background_img', 
        'screenshot1', 
        'screenshot2', 
        'screenshot3', 
        'screenshot4',
        'description', 
        'website_url', 
        'publisher', 
        'platforms', 
        'likes', 
        'dislikes',
        'release_date', 
        'genres', 
        'metacritic_points')