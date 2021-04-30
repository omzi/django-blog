from django.urls import path
# from . import views
from .views import HomeView, PostDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView

urlpatterns = [
    # path('', views.home, name='home'),
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/add/', AddPostView.as_view(), name='add-post'),
    path('category/add/', AddCategoryView.as_view(), name='add-category'),
    path('post/edit/<int:pk>/', UpdatePostView.as_view(), name='edit-post'),
    path('post/<int:pk>/delete/', DeletePostView.as_view(), name='delete-post'),
    path('category/<str:category>/', CategoryView, name='category'),
]