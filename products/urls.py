from django.urls import path

from products import views

urlpatterns = [
    path('', views.index, name='index'),  # Маршрут для отображения HTML-страницы
    path('api/products/', views.product_list),  # Маршрут для получения списка продуктов (GET)
    path('api/products/create/', views.product_create),  # Маршрут для создания продукта (POST)
]