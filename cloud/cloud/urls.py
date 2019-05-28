
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from login.views import user_login
from login.views import create_user
from login.views import add_user,auth_user
from feedpage.views import add_image,create_entry,show_images

urlpatterns = [
    path('',user_login),
    path('login/auth',auth_user),
    path('feedpage/',add_image),
    path('feedpage/show_images',show_images),
    path('feedpage/submit_image',create_entry),
    path('create/',add_user),
    path('create/submit_details',create_user),
    path('admin/', admin.site.urls),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
