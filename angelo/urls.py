from django.contrib import admin
from django.urls import path, include

from . import settings
from django.conf import settings
from django.conf.urls import static

from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    path('admin/', admin.site.urls),
    path('elarbol/', include('elarbol.urls')),
]



urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)