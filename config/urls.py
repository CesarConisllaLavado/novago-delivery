from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),

    path("productos/", include("apps.products.urls")),

    path(
        "",
        RedirectView.as_view(
            pattern_name="products:list",
            permanent=False,
        ),
    ),
]