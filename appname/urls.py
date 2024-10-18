from django.urls import path
from .views import index,feed,login,regspo,regus,spoboard,userboard,pay,logout,seefeed,sponsored,about
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',index,name='index'),
    path ('feed/',feed,name ="feed"),
    path ('seefeed/',seefeed,name="seefeed"),
    path ('login/',login,name="login"),
    path ('about/',about,name="about"),
    path ('logout/',logout, name="logout"),
    path ('regspo/',regspo, name="registers"),
    path ('regus/',regus, name="registeru"),
    path ('sponsored/',sponsored, name="sponsored"),
    path ('pay/<str:patient>/<str:uaddress>/<int:umobile_no>/<str:ulocation>/',pay,name="pay"),
    path('spoboard/',spoboard,name="sponsor_dashboard"),
    path ('userboard/',userboard,name="user_dashboard"),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)