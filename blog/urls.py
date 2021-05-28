from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='home'),
    path('<slug:slug>/', views.post_detail.as_view(), name='post_detail'),
    path('search', views.post_search, name='post_search'),
    path('create', views.PostCreate.as_view(), name='create_post'),
    path('edit/<slug:slug>', views.post_edit, name='edit_post'),
    path('signUp', views.signup, name='signup'),
    path('signIn', views.login_request, name='signin'),
    path('logout', views.logout_request, name='logout'),
    path('category/<str:category>', views.category_search, name='category_search'),
    path('wait', views.wait, name='wait'),
]
