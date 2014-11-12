from people.models import Person
from people.serializers import PersonSerializer
from rest_framework import viewsets, filters

class PersonViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    # Specify which fields to use for filtering, searching, and ordering
    filter_fields = ('id', 'first_name', 'last_name', 'age', 'github_acct', 'third_grade_grad_date',)
    search_fields = ('first_name', 'last_name', 'age', 'github_acct', 'third_grade_grad_date',)
    ordering_fields = ('first_name', 'last_name', 'age', 'github_acct', 'third_grade_grad_date',)