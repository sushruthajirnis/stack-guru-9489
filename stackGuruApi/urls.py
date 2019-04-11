from django.urls import path
from .views import ListSkillsView,createUserSkillsView


urlpatterns = [
    path('skills/', ListSkillsView.as_view(), name="skills-list"),
    path('skills/create',createUserSkillsView.as_view(),name='create-skill')
]