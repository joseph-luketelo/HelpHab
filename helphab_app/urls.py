from django.urls import path
from . import views

app_name = 'helphab_app'
urlpatterns = [
            path("", views.home_view,  name="home"),
            path("dashboard", views.login_view,  name="dashboard"),
            path("signup/", views.signup, name="signup"),
            path("login/", views.login_view,  name="login"),
            path("logout/", views.logout_view,  name="logout"),
            path("questions/", views.questions_view,  name="questions"),
            path("questions_list/", views.questions_list_view,  name="questions_list"),
            path("chatroom/<label>/", views.chat_room,  name="chatroom"),
        ]