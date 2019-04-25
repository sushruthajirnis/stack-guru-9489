from rest_framework import serializers
from .models import Skills
class FieldMixin(object):
    def get_field_names(self, *args, **kwargs):
        field_names = self.context.get('fields', None)
        if field_names:
            return field_names

        return super(FieldMixin, self).get_field_names(*args, **kwargs)

class SkillsSerializer(FieldMixin,serializers.ModelSerializer):
    class Meta:
        model=Skills
        fields=("user_name","skill_name")
