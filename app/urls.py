from django.urls import path,include
from .views import *
urlpatterns = [
    path('', landing , name='landing'),
    path('login/', login , name='login'),
    path('logout_view/', logout_view , name='logout_view'),
    path('register/', register , name='register'),
    path('forgot_password/',forgot_password, name="forgot_password"),
    path('home/', home, name='home'),
    path('manager_dashboard/', manager_dashboard, name='manager_dashboard'),
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
    path('admin_requested_accounts/', admin_requested_accounts, name='admin_requested_accounts'),
    path('admin_accept_requested_account/<int:id>/', admin_accept_requested_account, name='admin_accept_requested_account'),
    path('admin_reject_requested_account/<int:id>/', admin_reject_requested_account, name='admin_reject_requested_account'),
    path('admin_add_report/', admin_add_report, name='admin_add_report'),
    
]


