
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import home_page


# url patterns link into system
urlpatterns = [
    path("admin/", admin.site.urls),
    path('', home_page, name='home'),
    path('auth/', include('apps.account.urls', namespace='account')),
    path('team/', include('apps.team.urls', namespace='team')),
]
 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
