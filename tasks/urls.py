from django.urls import path, include
from rest_framework import routers
from tasks import views

router = routers.DefaultRouter()  #muestra el CRUD para usar en el postman
router.register(r'users', views.UserView, 'users')

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("api/v1/validate-credentials/", views.UserView.validateCredentials),
]