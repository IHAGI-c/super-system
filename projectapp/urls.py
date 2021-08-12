from django.urls import path

from projectapp.views import ProjectCreateView, ProjectDetailView

app_name = 'projectapp'

urlpatterns = [
    path('creat/', ProjectCreateView.as_view(), name='create'),
    path('detail/', ProjectDetailView.as_view(), name='detail'),

]
