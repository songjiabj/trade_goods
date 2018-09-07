from django.urls import path
from . import views
urlpatterns = [
    path('map/', views.map, name='map'),
    path('product/', views.product, name='product'),
    path('map/<str:category>/', views.mapCorB, name='mapCorB'),
    path('map/<str:category>/<str:l_category>/', views.mapCB, name='mapCB'),
    path('product/<str:category>/', views.productCorB, name='productCorB'),
    path('product/<str:category>/<str:l_category>/', views.productCB, name='productCB'),
]