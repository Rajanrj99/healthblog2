from django.urls import path
from django.contrib.auth import views as auth_views
from . import views  # Make sure to have the corresponding views in your views.py
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home, name='home'),  # Home page view
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  # Built-in login view
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),  # Built-in logout view
    path('signup/', views.signup, name='signup'),
    path('post/<int:pk>/', views.post_detail, name='post-detail'),# Assuming you have a signup view
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/edit-comment/<int:comment_id>/', views.post_detail, name='edit_comment'),
    path('delete-comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)