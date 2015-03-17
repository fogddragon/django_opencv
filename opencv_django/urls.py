from django.conf.urls import patterns, include, url
from opcv.views import ImageView, ImageListView, ImageAddView
from django.contrib import admin
from opencv_django import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'opencv_django.views.home', name='home'),
    url(r'^edit/(?P<id>\d+)$', ImageView.as_view(), name='image-edit'),
    url(r'^$', ImageListView.as_view()),
    url(r'^add/', ImageAddView.as_view(), name='add-image'),
    url(r'^admin/', include(admin.site.urls)),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                 {'document_root': settings.MEDIA_ROOT}),
)
