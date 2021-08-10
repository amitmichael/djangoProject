from django.urls import path
from . import views
from . import load_sample_data

urlpatterns = [
    path('', views.index, name='index'),
    path('<job_id>', views.find_candidates, name='find_candidates'),
]

