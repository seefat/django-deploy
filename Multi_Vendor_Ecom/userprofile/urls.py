from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup ,name='signup'),
    path('myaccount/', views.myaccount , name = 'myaccount'),
    path('my-store/',views.mystore, name = 'mystore'),
    path('my-store/add-product/',views.add_product, name='add_product'),
    path('my-store/edit-product/<int:pk>/',views.edit_product, name='edit_product'),
    path('my-store/delete-product/<int:pk>/',views.delete_product, name='delete_product'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='userprofile/login.html'), name='login'),
    path('vendors/<int:pk>/', views.vendor_detail, name='vendor_detail'),
]