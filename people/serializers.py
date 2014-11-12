from rest_framework import serializers
from people.models import Person
    
class PersonSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for people.models.Person
    """
    class Meta:
        model = Person
        fields = ('url', 'id', 'first_name', 'last_name', 'age', 'github_acct', 'third_grade_grad_date')