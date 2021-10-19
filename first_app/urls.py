from django.conf.urls import url
from first_app import views
#from first_project.first_app.views import index


urlpatterns = [
    url(r'^$',views.index,name= 'index'),
]