
from django.conf.urls import url, include
from django.contrib import admin
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^$', lambda r:redirect('shop:index'), name="root"),
    url(r'^shop/', include('shop.urls', namespace='shop')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )
