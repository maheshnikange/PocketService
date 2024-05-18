from django.urls import path
from . import views


urlpatterns = [
    path('', views.index , name='index'),
    path('login/', views.login , name='login_page'),
    path('register/', views.register , name='register_page'),
    path('category-services/<int:cat_id>/', views.get_admin_category_services, name='get_admin_category_services'),
    path('service-shops/<int:service_id>/', views.get_service_shop, name='get_service_shop'),
]
