from django.db import models

class Person(models.Model):
    """
    Model for Person objects, which include names and 
    """
    # Since 'id' is a field defined in our data set, we need to set up a different primary key here,
    # otherwise Django will automatically create a PK field named 'id' that isn't editable
    person_db_key = models.AutoField(primary_key=True)
    id = models.PositiveIntegerField(blank=False)
    created = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    github_acct = models.CharField(max_length=100, blank=True)
    third_grade_grad_date = models.DateField(null=True, blank=True)
     
    class Meta:
        ordering = ('created',)