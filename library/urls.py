from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path
from lib.views import uploadbook,booklist,tagview
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("",uploadbook),
    path("booklist/uploadbook",uploadbook),
    path("booklist",booklist),
    path("tags/<slug:tag_slug>/",tagview.as_view(),name='tagview')]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
