from django.urls import path
from .views import RecipeList, RecipeDetail, RecipeCreate, RecipeUpdate, RecipeDelete

urlpatterns = [
    path('', RecipeList.as_view(), name='recipe_list'),
    path('recipe/<int:pk>/', RecipeDetail.as_view(), name='recipe_detail'),
    path('recipe/new/', RecipeCreate.as_view(), name='recipe_create'),
    path('recipe/<int:pk>/edit/', RecipeUpdate.as_view(), name='recipe_edit'),
    path('recipe/<int:pk>/delete/', RecipeDelete.as_view(), name='recipe_delete'),
]