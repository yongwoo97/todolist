from django.urls import path, include
from .views import TodoListMonthView, TodoListDayView, TodoListDetailView

urlpatterns = [
    path('<int:year>/<int:month>/', TodoListMonthView.as_view()),
    path('<int:year>/<int:month>/<int:day>/', TodoListDayView.as_view()),
    path('detail/<int:pk>/', TodoListDetailView.as_view())
]