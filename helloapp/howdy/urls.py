from django.conf.urls import url
from howdy import views


urlpatterns = [
    url(r'^$', views.AboutPageView.as_view()),
    url(r'^about/$', views.HomePageView.as_view()),
]
