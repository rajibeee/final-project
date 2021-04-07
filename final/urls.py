
from django.contrib import admin
from django.urls import include,path
from bookStore import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('book-store/', views.index,name='index'),
    path('book-store/signIn/', views.signIn,name='signIn'),
    path('book-store/signUp/', views.signUp,name='signUp'),
    path('',include("django.contrib.auth.urls")),
]
