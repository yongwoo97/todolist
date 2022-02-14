from rest_framework import serializers
from .models import todolist

class TodoSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='username.username')
    class Meta:
        model = todolist
        fields = ('date','username', 'title', 'repeat',)
