from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Recipe
from .forms import RecipeForm

class RecipeList(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipe_app/recipe_list.html'
    context_object_name = 'recipes'

    def get_queryset(self):
        return Recipe.objects.filter(user=self.request.user)

class RecipeDetail(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipe_app/recipe_detail.html'

class RecipeCreate(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipe_app/recipe_form.html'
    success_url = reverse_lazy('recipe_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class RecipeUpdate(LoginRequiredMixin, UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipe_app/recipe_edit.html'
    success_url = reverse_lazy('recipe_list')

    def get_queryset(self):
        return Recipe.objects.filter(user=self.request.user)

class RecipeDelete(LoginRequiredMixin, DeleteView):
    model = Recipe
    template_name = 'recipe_app/recipe_delete.html'
    success_url = reverse_lazy('recipe_list')

    def get_queryset(self):
        return Recipe.objects.filter(user=self.request.user)