from django.urls import path
from .import views

app_name = 'crud_app'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('list/', views.SchoolList.as_view(), name='list'),
    path('detail/<int:pk>/', views.SchoolDetail.as_view(), name='detail'),
    path('update/<int:pk>/', views.SchoolUpdate.as_view(), name='update'),
    path('create/', views.SchoolCreate.as_view(), name='create'),
    path('delete/<int:pk>/', views.SchoolDelete.as_view(), name='delete'),
]
