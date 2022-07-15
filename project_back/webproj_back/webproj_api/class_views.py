from django.shortcuts import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated

from webproj_api.serializers import GSerializer, GImgsSerializer, GDescSerializer, GDetsSerializer, AllSerializer
from webproj_api.serializers import Game2Serializer, GameImages2Serializer, GameDescription2Serializer, GameDetails2Serializer, All2Serializer
from webproj_api.models import Game, GameImages, GameDescription, GameDetails


class GameListAPIView(APIView):
    def get(self, request):
        games = Game.objects.all()
        serializer = GSerializer(games, many=True)
        permission_classes = (IsAuthenticated,)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = GSerializer(data=request.data)
        permission_classes = (IsAuthenticated,)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GameDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Game.objects.all().select_related('game_id').get(id=pk)
        except Game.DoesNotExist as e:
            raise Http404

    def get(self, request, pk=None):
        all = self.get_object(pk)
        serializer = All2Serializer(all)
        permission_classes = (IsAuthenticated,)
        return Response(serializer.data)

    def put(self, request, pk=None):
        permission_classes = (IsAuthenticated,)
        all = self.get_object(pk)
        serializer = All2Serializer(instance=all, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk=None):
        permission_classes = (IsAuthenticated,)
        all = self.get_object(pk)
        all.delete()
        return Response({'message': 'deleted'}, status=204)

