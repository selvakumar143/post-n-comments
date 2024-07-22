# your_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.post_form_view, name='post_form_view'),
    path('list/', views.post_list_view.as_view(), name='post_list_view'),
    path('<slug:slug>/', views.detail_view.as_view(), name='detail'),
    # path('<slug:slug>/', views.detail_view.as_view(), name='detail'),  # Using slug
]
