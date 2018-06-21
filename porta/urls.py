from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^maps', views.landing_page, name='landing_page'),
    url(r'^gyms', views.gyms, name='gyms'),
    url(r'^blog', views.blog, name='blog')

]