from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import signup, custom_logout, login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipe_app.urls')),
    path('accounts/login/', login_view, name='login'),
    path('accounts/logout/', custom_logout, name='logout'),
    path('accounts/signup/', signup, name='signup'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)