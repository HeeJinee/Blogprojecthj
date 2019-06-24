from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('<int:blog_id>',views.detail, name="detail"),
    path('create', views.create, name="create"), 
    path('edit/<int:blog_id>', views.edit, name="edit"),
    path('delete/<int:blog_id>', views.delete, name="delete"),
    path('comment_add/<int:blog_id>', views.comment_add, name='comment_add'),
    path('comment_edit/<int:comment_id>', views.comment_edit, name='comment_edit'),
    path('comment_delete/<int:comment_id>', views.comment_delete, name='comment_delete'),
    
]