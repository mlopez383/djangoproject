from django.conf.urls import include, url
from django.contrib import admin
from login import views as views_l
from home import views as views_h

urlpatterns = [
    url(r'^$', views_h.init, name='init'),
    url(r'^logout/', views_l.logout, name='logout'),
    url(r'^dashboard/', include('dashboard.urls')),
    url(r'^profile/', include('profile_page.urls')),
    url(r'^admin/', admin.site.urls),
]