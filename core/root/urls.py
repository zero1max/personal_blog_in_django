from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('article/<int:id>/', views.article_detail, name='article_detail'),
    path('admin-panel/', views.admin_home, name='admin_home'),
    path('edit/<int:id>/', views.edit_article, name='edit_article'),
    path('new/', views.new_article, name='new_article'),
    path('delete/<int:id>/', views.delete_article, name='delete_article'),
]
