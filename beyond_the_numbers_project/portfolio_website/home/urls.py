from django.contrib import admin
from django.urls import path, include
from . import views
from .views_api import views_api

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",views.home, name='home'),
    path("about/",views.about, name='about'),
    path("project/",views.project, name='project'),
    path("contact/",views.contact, name='contact'),
    path("sets",views.movies, name='movies'),
    path("fetch_html",views_api.my_view,name='my_view'),
    path("api/",views_api.MatchesListApiView.as_view(),name='MatchesListApiView')
]



