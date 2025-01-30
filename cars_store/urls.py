from django.urls import path
from . import views

urlpatterns = [
    path('', views.category_list, name="category_list"),
    path('category/new', views.create_category, name="create_category"),
    path('category/<int:pk>/good/new', views.create_good, name="create_good"),
    path('category/<int:c_pk>/good/<int:g_pk>', views.good_detail, name="good_detail"),
    path('category/<int:pk>', views.category_detail, name="category_detail"),
]
