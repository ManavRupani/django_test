from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('blog',views.blog),
    path('me',views.me),
    path('blog/<int:id_json>/',views.blog_ind,name='blog_ind')

]
