from django.db import models
from cuser.models import User

class todolist(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(null=False, blank=False)
    title = models.CharField(max_length=1000, null=False)
    repeat = models.IntegerField(default=0)
