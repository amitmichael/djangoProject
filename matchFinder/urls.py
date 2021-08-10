from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<job_id>', views.find_candidates, name='find_candidates'),

]

