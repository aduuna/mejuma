from django.db import models

from mejuma.users.models import User

# Create your models here.


class Job(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    budget = models.FloatField(default=0.0)
    duration = models.DurationField()
    slots = models.IntegerField('No. of People', default=1)
    location = models.CharField(max_length=128)  # work on this
    deadline = models.DateTimeField()
    pub_date = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class JobApplicants(models.Model):
    applicant = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        null=True, blank=True
    )
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    date_applied = models.DateTimeField(auto_now_add=True)


class JobAllocation(models.Model):
    taken_by = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        null=True, blank=True
    )
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    date_taken = models.DateTimeField(auto_now_add=True)
