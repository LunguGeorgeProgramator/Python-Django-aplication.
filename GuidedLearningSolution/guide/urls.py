from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from guide.views import GuideViews

from . import views
from .views import GuideViews, GuideDetails

urlpatterns = [
    path('', GuideViews.as_view()),
    path('details', GuideDetails.as_view()),
    # path('home/', GuideViews.as_view(name='home')),
    # path('details/', views.details, name='details')
]