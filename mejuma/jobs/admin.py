from django.contrib import admin

from .models import Job, JobAllocation, JobApplicants
# Register your models here.


admin.site.register(Job)
admin.site.register(JobApplicants)
admin.site.register(JobAllocation)
