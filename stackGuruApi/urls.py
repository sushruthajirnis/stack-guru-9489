from django.urls import path
from .views import ListSkillsView,createUserSkillsView,getUserSkillsView

urlpatterns = [
    path('skills/', ListSkillsView.as_view(), name="skills-list"),
    path('skills/create',createUserSkillsView.as_view(),name='create-skill'),
    path('skills/<user_name>/',getUserSkillsView.as_view(),name='skill-user')
]