from django.urls import path

from restapi_app import views

urlpatterns=[
    path('login',views.LoginView,name='login'),
    path('User_Registrations',views.User_Registrations,name='User_Registrations'),
    path('addprofiledata/<int:user_id>',views.profileDetails,name='addprofiledata'),
    path('',views.Viewhome,name='home'),
    path('login_view',views.homelogin,name='login_view'),
    path('Registration_page',views.RegistrationPage,name='Registration_page'),
    path('profile_page',views.ProfilePage,name='profile_page'),
    path('view_profile',views.view_profile,name='view_profile')

]