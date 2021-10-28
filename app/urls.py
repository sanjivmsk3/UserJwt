from django.urls import path
from app.views import *

urlpatterns= [
    path('', Home.as_view(), name='home'),
    path('signup', SignUp.as_view(), name='signup'),
    path('logout', LogOut.as_view(), name='logout'),
    path('user-details', User_Details.as_view(), name='user_details'),
    path('delete-user/<int:id>', DeleteUser.as_view(), name='delete_user'),
    path('user-detail-edit/<int:pk>', User_Detail_Edit.as_view(), name='user_detail_edit'),
]