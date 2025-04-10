from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('add/', views.add, name='add'),
    path('search/', views.search, name='search'),
    path('edit/<slug:category_slug>/<slug:slug>', views.edit, name='edit'),
    path('categories/', views.categories, name='categories'),
    path('drafts/', views.drafts, name='drafts'),
    path('<slug:category_slug>/<slug:slug>/', views.detail, name='post_detail'),
    path('<slug:slug>/', views.category, name='category_detail'),
    path('', views.frontpage, name='frontpage'),
]
