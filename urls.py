from django.urls import path
from.import views
from .views import download_file


urlpatterns=[
    path('',views.login,name='loginurl'),
    path('filelist/',views.displayfileslist,name='filelisturl'),
    path('signup/',views.signupUser,name='signupurl'),
    path('insert/',views.insertfile,name='inserturl'),
    path('download/<int:fileid>/', download_file, name='download_file'),
    
]