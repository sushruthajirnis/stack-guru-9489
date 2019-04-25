from rest_framework import generics
from .models import Skills
from rest_framework.response import Response
from rest_framework.views import status
from .serializers import SkillsSerializer


# Create your views here.

class ListSkillsView(generics.ListAPIView):
    """
    Provides a way to view all skill list 
    with names

    """
    queryset=Skills.objects.all()
    serializer_class=SkillsSerializer


class createUserSkillsView(generics.CreateAPIView):
    """
    Provides a way to create skills :)
    """
    serializer_class=SkillsSerializer
    def post(self,request,*args,**kwargs):
        user_name=request.data.get("user_name","")
        skill_name=request.data.get("skill_name","")
        if not user_name or not skill_name:
            return Response(
                data={
                    "message": "username and skill name required"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        new_user_skill=Skills.objects.create(user_name=user_name,skill_name=skill_name)
        return Response(data=SkillsSerializer(new_user_skill).data,status=status.HTTP_201_CREATED)

class getUserSkillsView(generics.RetrieveAPIView):
    """
    Provides a way to retrieve a particular a skill and get
    links to so

    """
    serializer_class=SkillsSerializer
    lookup_field='user_name'
    queryset=Skills.objects.all()

    def get(self,request,*args,**kwargs):
        s_object=self.get_object()
        a_object=SkillsSerializer(s_object).data
        return Response(data=SkillsSerializer(a_object,context={'fields':['skill_name']}).data,status=status.HTTP_200_OK)