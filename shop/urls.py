from django.urls import path
from . import views

urlpatterns = [
    path('',views.landing,name='landing'),
    path('category_list/',views.category_list,name='category_list'),
    path('<slug:category_slug>/',views.subcategory_list,name='subcategory_list'),
    path('<slug:category_slug>/<slug:subcategory_slug>/',views.product_list,name='product_list'),

]