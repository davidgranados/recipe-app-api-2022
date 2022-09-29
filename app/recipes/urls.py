"""
URL mappings fot the recipes app.
"""
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from recipes import views

router = DefaultRouter()
router.register("tags", views.TagViewSet)
router.register("ingredients", views.IngredientViewSet)
router.register("", views.RecipeViewSet)

app_name = "recipes"

urlpatterns = [
    path("", include(router.urls)),
]
