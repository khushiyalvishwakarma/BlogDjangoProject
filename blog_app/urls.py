from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.homefun),
    path('home',views.homefun),
    path('addblog',views.blogfun),
    path('insertblog',views.insert_blog),
    path('displayblog',views.display_blog),
    path('edit/<int:id>', views.editblog),
    path('updatedata/<int:id>', views.update_fun),
    path('delete/<int:id>', views.delete_fun),
    path('search', views.search)


]