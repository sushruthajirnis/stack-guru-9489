from rest_framework import generics
from .models import Skills
from .serializers import SkillsSerializer


# Create your views here.

class ListSkillsView(generics.ListAPIView):
    """
    Provides a way to view all skill list 
    with names

    """
    queryset=Skills.objects.all()
    serializer_class=SkillsSerializer