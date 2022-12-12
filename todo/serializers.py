from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .models import Todo
# Serializers define the API representation.
class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        fields = ['id','title', 'description', 'created_at']