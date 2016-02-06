from django.conf.urls import include, url
from django.contrib import admin
from login import views

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^dashboard/', include('dashboard.urls')),
    url(r'^admin/', admin.site.urls),
]