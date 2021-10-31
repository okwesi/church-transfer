from django.contrib import admin
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url('^transfers/', include('transfers.urls')),
    url('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
