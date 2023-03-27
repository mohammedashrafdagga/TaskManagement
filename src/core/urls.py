
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


# url patterns link into system
urlpatterns = [
    path("admin/", admin.site.urls),
    path('api-auth/', include('apps.account.urls', namespace='account')),
    path('api-team/', include('apps.team.urls', namespace='team')),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
