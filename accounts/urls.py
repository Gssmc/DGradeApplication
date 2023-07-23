
from django.urls import path
from accounts.views import (SignUpView,LogoutView,
        LoginView,ProfileView,DeleteGarbageView,DeleteGarbageOrderView)

urlpatterns = [
    path('signup/',SignUpView,name="signup"),
    path('signup/<int:id>/',SignUpView,name="signup"),
    path('logout/',LogoutView,name='logout'),
    path('login/', LoginView,name="login"),
    path('user_profile/<int:id>/',ProfileView,name='profile'),
    path('delete_garbage/<int:id>/',DeleteGarbageView,name='delete_garbage'),
    path('delete_garbage_order/<int:buyer_id>/<int:garbage_id>/',DeleteGarbageOrderView,name='delete_garbage_order'),
]
