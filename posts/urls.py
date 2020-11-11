from django.urls import path
from . import views

app_name='posts'
urlpatterns= [
    path('index/', views.index, name='index'),
    path('', views.index, name='index'),
    path('table/', views.table, name='table'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:post_id>/edit/', views.edit, name='edit'),
    path('<int:post_id>/update/', views.update, name='update'),
    path('<int:post_id>/delete/', views.delete, name='delete'),
    path('post_gaebalja/', views.filter_gaebalja, name='post_gaebalja'),
    path('<int:post_id>/like/', views.like, name='like'),
]