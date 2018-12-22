from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls import  include, url
from mysite import views as mysite_views



admin.autodiscover()


urlpatterns = [
    url('^admin/', admin.site.urls),
    url('^login/', auth_views.LoginView.as_view(template_name="mysite/login.html"), name="login"),
    url('^signup/', mysite_views.signup, name='signup'),
    url('', include('boot.urls')),
    url('', include('rental_system.urls')),


]


