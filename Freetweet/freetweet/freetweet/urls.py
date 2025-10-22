"""
URL configuration for freetweet project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

# --- Imports for our custom views and forms ---
from tweet import views as tweet_views
from tweet.forms import LoginForm # Make sure LoginForm is defined in tweet/forms.py

urlpatterns = [
    path('admin/', admin.site.urls),

    # --- Homepage ---
    path('', tweet_views.tweet_list, name='tweet_list_root'),

    # --- App URLs ---
    path('tweet/', include('tweet.urls')),

    # --- Custom Auth URLs ---
    path('register/', tweet_views.register, name='register'),

    path('login/', auth_views.LoginView.as_view(
        template_name='registration/login.html',
        authentication_form=LoginForm
    ), name='login'), # URL name used in settings.LOGIN_URL

    path('logout/', auth_views.LogoutView.as_view(
        next_page='tweet_list_root', # Redirect target after logout
        http_method_names = ['get', 'post', 'options'] # Allow GET for logout link
    ), name='logout'),

    # --- DO NOT INCLUDE THIS LINE if you define login/logout manually ---
    # path('accounts/', include('django.contrib.auth.urls')),
]

# --- Media Files Handling (for development) ---
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

