from django.conf.urls import url

from .views import PackageCreateView


urlpatterns = [
    url(r'^create/$', PackageCreateView.as_view())
]
