from django.urls import path, include
from .views import TodoListMonthView, TodoListDayView, TodoListDetailView, TodoListOnlyCheckView

urlpatterns = [
    path('<int:year>/<int:month>/', TodoListMonthView.as_view()),
    path('<int:year>/<int:month>/<int:day>/', TodoListDayView.as_view()),
    path('<int:year>/<int:month>/<int:day>/<int:pk>/', TodoListDetailView.as_view()),
    path('<int:year>/<int:month>/<int:day>/<int:pk>/only/', TodoListOnlyCheckView.as_view())
]