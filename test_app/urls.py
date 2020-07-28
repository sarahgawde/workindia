from django.urls import path, include
from test_app import views 
 
urlpatterns = [ 
	path('user/auth/',views.user_login),
    path('user/',views.user_register),
    path('sites/list/<int:pk>/', views.notes_list),
    path('sites/<int:pk>/',views.get_user_info)
]