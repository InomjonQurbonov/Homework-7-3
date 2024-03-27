from django.urls import path

from user.views import (register_view, login_view,
                        logout_view, change_password,
                        confirm_email, confirm_email_confirm
                        )

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='log_out'),
    path('change_password/', change_password, name='change_password'),
    path('confirm_email/', confirm_email, name='confirm_email'),
    path('confirm_email_confirm/', confirm_email_confirm, name='confirm_email_confirm')
]
