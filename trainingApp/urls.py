from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from .views import IndexView, DeployDetailView, next_deploy, prev_deploy, ResultsView, signup, home

from . import views

app_name = 'trainingApp'

urlpatterns = [
    path("", views.home, name='home'),
    path("training/", login_required(IndexView.as_view()), name="training"), 
    path("<int:deploy_id>/",  login_required(DeployDetailView.as_view()), name="forms"),
    path("next/", views.next_deploy, name="next"),
    path("prev/", views.prev_deploy, name="prev"),
    path("results/", views.ResultsView.as_view(), name="results"),
    
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
]