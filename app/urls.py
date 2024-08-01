from django.urls import path
from .views import index_list, index_detail, index_create, index_update, index_delete

urlpatterns = [
    path('', index_list, name='index_list'),
    path('<int:pk>/', index_detail, name='index_detail'),
    path('create/', index_create, name='index_create'),
    path('<int:pk>/update/', index_update, name='index_update'),
    path('<int:pk>/delete/', index_delete, name='index_delete'),
]