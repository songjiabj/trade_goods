from django.urls import path
from . import views

urlpatterns = [
    path('map/', views.map, name='map'),
    path('home/', views.home, name='home'),
    path('product/', views.product, name='product'),
    path('map/c00/', views.mapC00, name='mapC00'),
    path('map/b00/', views.mapB00, name='mapB00'),
    path('map/c00/b00/', views.map, name='map'),
    path('map/<str:category>/', views.mapCorB, name='mapCorB'),
    path('map/<str:category>/<str:l_category>/', views.mapCB, name='mapCB'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]