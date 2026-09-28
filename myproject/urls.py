from django.urls import path
from . import views

app_name = 'onlinecourse'

urlpatterns = [
    path("admin/", admin.site.urls),
]
    
     