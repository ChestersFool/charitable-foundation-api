"""
URL configuration for cfAPI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from help_requests.views import HelpRequestAPIView, HelpRequestCreateView
from news.views import NewsAPIView, NewsDetailView
from user.views import UserAPIView, UserCreateView
from event.views import EventAPIView, EventDetailView
from user_event.views import RegisterForEventView
from volunteer_application.views import VolunteerApplicationAPIView, VolunteerApplicationCreateView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/eventslist/', EventAPIView.as_view()), # GET
    path('api/event/<int:event_id>/', EventDetailView.as_view()), # GET
    path('api/register_for_event/', RegisterForEventView.as_view()), # POST

    path('api/help_requestlist/', HelpRequestAPIView.as_view()), # GET
    path('api/help_request_create/', HelpRequestCreateView.as_view()), # POST

    path('api/volunteer_applicationlist/', VolunteerApplicationAPIView.as_view()), # GET
    path('api/volunteer_application_create/', VolunteerApplicationCreateView.as_view()), # POST

    path('api/userslist/', UserAPIView.as_view()), # GET
    path('api/user_create/', UserCreateView.as_view()), # POST

    path('api/newslist/', NewsAPIView.as_view()), # GET
    path('api/news/<int:news_id>/', NewsDetailView.as_view()), # GET
]

urlpatterns = format_suffix_patterns(urlpatterns)
