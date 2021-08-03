from django.urls import path
from . import views

urlpatterns = [
    path('', views.index2),  # 1
    path('checkout', views.check),
    path('allproducts', views.allproducts),  # 2
    path("myproducts", views.myproducts),
    path("mycart", views.mycart),
    path('products/<int:product_id>/add', views.add_to_cart),  # 6
    path('remove/<int:product_id>', views.remove_product),  # 4
    path('mycart1', views.mycart1),
    path('mycart2', views.mycart2),
    path('mycart3', views.mycart3),
    path('mycart4', views.mycart4),
    path('mycart5', views.mycart5),
    path('mycart6', views.mycart6),
    path('mycart7', views.mycart7),
    path('mycart8', views.mycart8),
    path('mycart9', views.mycart9),
    path('mycart10', views.mycart10),
    path('mycart11', views.mycart11),
    path('mycart12', views.mycart12),
]
