from django.urls import path
from . import views

app_name = "board"

urlpatterns = [
    path("list", views.board_list, name = 'list'),
    path('write', views.board_write, name = 'write'),
    path('detail/<int:id>/', views.board_detail, name = 'detail')
]