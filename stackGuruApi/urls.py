from django.urls import path
from .views import ListSkillsView


urlpatterns = [
    path('skills/', ListSkillsView.as_view(), name="skills-list")
]