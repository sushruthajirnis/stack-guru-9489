from django.urls import reverse
from rest_framework.test import APITestCase,APIClient
from rest_framework.views import status
from stackGuruApi.models import Skills
from stackGuruApi.serializers import SkillsSerializer
from .dbtest import databases as testdb

# Create your tests here.

class BaseViewTest(APITestCase):
    client=APIClient()
    # default tests are allowed to run on all databases
    # locally you may want to change the mirror
    databases=testdb
    @staticmethod
    def create_skill(user_name="",skill_name=""):
        if user_name!="" and skill_name!="":
            Skills.objects.create(user_name=user_name,skill_name=skill_name)

    def setUp(self):
        self.create_skill("shajirnis","karate")


class GetAllSkills(BaseViewTest):
    def test_get_all_skills(self):
        """
        Test to get all skills in the db

        """
        #endpoint all
        response=self.client.get(reverse("skills-list",kwargs={"version":"v1"}))

        #make fetch
        expected = Skills.objects.all()
        print(response.data)
        serialized=SkillsSerializer(expected,many=True)
        self.assertEqual(response.data,serialized.data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
