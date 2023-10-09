from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from store.views import PackViewSet, SampleViewSet, LabelViewSet, RelationView, DownloadSampleView, BuyingSampleView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'label', LabelViewSet)
router.register(r'pack', PackViewSet, basename='pack')
router.register(r'sample', SampleViewSet, basename='sample')
router.register(r'relation', RelationView)
router.register(r'buying', BuyingSampleView, basename="buying")

urlpatterns = [
                  # path('', main_page),
                  path('admin/', admin.site.urls),
                  path('api/', include(router.urls)),
                  path('api/auth/', include('djoser.urls')),
                  path('api/auth/', include('djoser.urls.authtoken')),
                  path('api/sample/download/<int:pk>', DownloadSampleView.as_view())
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
