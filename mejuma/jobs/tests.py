from datetime import timedelta

import django.test
# from django.test.utils import setup_test_environment
from django.utils import timezone

from mejuma.users.models import User
from .models import Job


# Create your tests here.


def create_sample_user(*args, **kwargs):
    user = User(username='random', password='dfhfhfa755')
    user.save()
    return user


def create_sample_job(*args, **kwargs):
    job = Job(
        title='Awesome job',
        description=('this is the coolest Job on the planet'
                     'Take this  Job and make Billions without'
                     'having any prior experience.'
                     'You will Never have to work AGAIN!'
                     ),
        duration=timedelta(7),
        deadline=timezone.now() + timedelta(30),
        posted_by=create_sample_user()
    )

    return job


class TestJobModel(django.test.TestCase):
    def test_job_creation_with_default_sample(self):
        """Test that model Job instanncce creation works when
        all required argument are provided
        """
        # setup_test_environment()
        job = create_sample_job()
        job.save()
        all_jobs = Job.objects.all()

        self.assertQuerysetEqual(all_jobs, ['<Job: {}>'.format(str(job))])
