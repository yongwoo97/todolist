from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import todolist
from .serializer import TodoSerializer, TodoOnlySerializer

#데코레이터 보단 super를 사용하는게 더 좋겠지?
def decorator(func):
    def wrapper(self, request, *args, **kwargs):
        request.data['date'] += ' 00:00:00'
        return func(self, request, *args, **kwargs)
    return wrapper


class TodoListMonthView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = todolist.objects.all()
    serializer_class = TodoSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        year, month = kwargs['year'], kwargs['month']
        user_only_queryset = queryset.filter(username=request.user).filter(date__year=year,
                                                                           date__month=month)
        #여기 아래 코드에서 many=True는 다수의 쿼리셋을 시리얼라이즈 하겠다는 의미
        serializer = self.get_serializer(user_only_queryset, many=True)
        #response는 에러처리도 다해주나?
        #
        #아래 for문을 효율적으로 대체하는 방법은 없을까?
        for i in serializer.data:
            i['date'] = i['date'][:10]

        return Response(serializer.data[::-1])

    def create(self, request, *args, **kwargs):
        request.data['date'] += ' 00:00:00'
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(username=self.request.user)

class TodoListDayView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = todolist.objects.all()
    serializer_class = TodoSerializer
    #이거보다 더 좋은 방법은 없을까?
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        year, month, day = kwargs['year'], kwargs['month'], kwargs['day']
        user_only_queryset = queryset.filter(username=request.user).filter(date__year=year,
                                                                           date__month=month,
                                                                           date__day=day)
        serializer = self.get_serializer(user_only_queryset, many=True)

        for i in serializer.data:
            i['date'] = i['date'][:10]
        return Response(serializer.data[::-1])

    def create(self, request, *args, **kwargs):
        request.data['date'] += ' 00:00:00'
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(username=self.request.user)

class TodoListDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = todolist.objects.all()
    serializer_class = TodoSerializer

    def update(self, request, *args, **kwargs):
        request.data['date'] += ' 00:00:00'
        return super().update(request, *args, **kwargs)

class TodoListOnlyCheckView(generics.RetrieveUpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = todolist.objects.all()
    serializer_class = TodoOnlySerializer