from django.urls import path

from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('catagory/<int:catagory_id>/', views.product_list, name='category_detail_id'),
    # path('catagories/', views.product_list, name='catagories'),
    path('product_detail/<int:product_id>', views.product_detail, name='product_detail'),
    path('product/<int:product_id>/add-comment',views.add_comment,name = 'add_comment'),
    path('product/<int:product_id>/add_order',views.add_order,name ='add_order')
]
