from django.conf.urls import url
from . import views
urlpatterns = [
url(r'^create/note/(?P<lead_id>\d+)$', views.createNote),
url(r'^edit/(?P<lead_id>\d+)$', views.renderEdit),
url(r'^edit/(?P<lead_id>\d+)/submit$', views.editLead),
url(r'^delete/(?P<lead_id>\d+)$', views.deleteLead),
url(r'^view/(?P<lead_id>\d+)$', views.leadProfile),
url(r'^favorite/(?P<lead_id>\d+)$', views.favoriteLead),
url(r'^unfavorite/(?P<lead_id>\d+)$', views.deleteFav),
url(r'^favorites$', views.renderFav),
url(r'^add$', views.addLead),
url(r'^create$', views.renderNewLead),
url(r'^$', views.index)
]