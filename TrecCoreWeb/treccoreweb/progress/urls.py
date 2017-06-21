from django.conf.urls import url
from django.views.generic import TemplateView

from treccoreweb.progress import views

urlpatterns = [
    url(r'^$', views.Home.as_view(),
        name='home'),
    url(r'^tutorial/$', TemplateView.as_view(template_name="progress/tutorial.html"),
        name='tutorial'),
    url(r'^pretask/$', views.PretaskView.as_view(),
        name='pretask'),
    url(r'^posttask/$', views.PosttaskView.as_view(),
        name='posttask'),
    url(r'^exit/$', TemplateView.as_view(template_name="progress/exit.html"),
        name='exit'),

]
