from django.db import models

# Create your models here.
class Skills(models.Model):
  user_name=models.CharField(max_length=50)
  skill_name=models.CharField(max_length=60)
