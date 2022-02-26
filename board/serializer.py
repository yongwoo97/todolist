from rest_framework import serializers
from .models import todolist

class TodoSerializer(serializers.ModelSerializer):
    #여기서 read only 필드로 설정해주어야 하는 이유는 무엇이었지?
    #왜 기억이 안나지?
    #시리얼라이저에서 perform create 하기전에 is valid를 하기 때문에 readonly설정이 필요하다
    username = serializers.ReadOnlyField(source='username.username')
    class Meta:
        model = todolist
        fields = ('id', 'username', 'date', 'title', 'repeat', 'importance',)
