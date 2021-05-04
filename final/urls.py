
from django.contrib import admin
from django.urls import include,path
from bookStore import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('book-store/', views.index,name='index'),
    path('book-store/signIn/', views.signIn,name='signIn'),
    path('book-store/signUp/', views.signUp,name='signUp'),
    path('book-store/signOut/', views.signOut,name='signOut'),
    path('book-store/myProfile/', views.myProfile,name='myProfile'),
    path('book-store/store/', views.store,name='store'),
    path('store/<int:id>/',views.bookDetails,name='bookDetails'),
    path('',include("django.contrib.auth.urls")),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
