from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import get_object_or_404, redirect
from django.urls import include, path

from recipes.models import Recipe


def short_link_redirect(request, short_link):
    recipe = get_object_or_404(Recipe, short_link=short_link)
    return redirect(f'/recipes/{recipe.id}')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('s/<str:short_link>/', short_link_redirect, name='short_link'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
