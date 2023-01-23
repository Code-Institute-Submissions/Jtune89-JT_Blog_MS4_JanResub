from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('update/<int:pk>/', views.UpdateComment.as_view(), name='update'),
    path('delete_comment/<int:pk>/', views.DeleteComment.as_view(), name='delete_comment'),
]
