from django.urls import path
from .views import HomeView , PostView , AboutView, ContactView

urlpatterns = [

  path('', HomeView.as_view(), name='blog-home'),
  path('post/<int:pk>/', PostView.as_view(), name='post_detail'),
  path('about/', AboutView.as_view(), name='about_page'),
  path('contact/', ContactView.as_view(), name='contact'),
]
