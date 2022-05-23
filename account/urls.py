from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    # This path contains all Django auth (login/out, change/reset passwords) 
    path('', include('django.contrib.auth.urls')),

    # Registering
    path('register/', views.register, name='register'),

    # Dashboard
    path('', views.dashboard, name='dashboard'),
]





























# Django authentication URL patterns
# urlpatterns = [
#     # Login and Logout
#     # path('login/', views.user_login, name='login'),
#     # path('login/', auth_views.LoginView.as_view(), name='login'),
#     # path('logout/', auth_views.LogoutView.as_view(), name='logout'),

#     # # Change passwords
#     # path('password_change', auth_views.PasswordChangeView.as_view(), name='password_change'),
#     # path('password_change/done', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

#     # # Reset passwords
#     # path('password_reset', auth_views.PasswordResetView.as_view(), name='password_reset'),
#     # path('password_reset/done', auth_views.PasswordResetDoneView.as_view(), 
#               name='password_reset_done'
#       ),
#     # path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(),
#               name='password_reset_confirm'
#       ),
#     # path( 'reset/done', auth_views.PasswordResetCompleteView.as_view(),
#               name='password_reset_complete'
#       ),
# ]
