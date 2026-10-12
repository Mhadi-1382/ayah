from django.urls import path
from auth_app import views

urlpatterns = [
    path('signup/', view=views.signup_view, name='signup'),
    path('signin/', view=views.signin_view, name='signin'),
    path('profile/signout/', view=views.signout_view, name='signout'),
    path('profile/edit/', view=views.profile_edit_view, name='profile_edit'),
]
