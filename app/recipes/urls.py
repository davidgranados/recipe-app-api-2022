"""
URL mappings fot the recipes app.
"""
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from recipes import views

router = DefaultRouter()
router.register("recipes", views.RecipeViewSet, basename="recipes")

app_name = "recipes"

urlpatterns = [
    path("", include(router.urls)),
]
