from django.urls import path, include
from . import views
from blog.views import HomeView, PostView, PostbroView
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', PostView.as_view(), name='art-detail'),
    path('postbro/', PostbroView.as_view(), name='postbro'),
]
