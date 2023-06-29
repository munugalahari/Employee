from django.test import TestCase
from rest_framework.test import APIClient
from .models import Employee
from faker import Faker

fake = Faker()


class EmployeeAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.employee1 = Employee.objects.create(
            name=fake.name(),
            position=fake.job_title(),
            office=fake.city(),
            age=fake.random_int(min=18, max=65),
            start_date=fake.date_between(start_date='-10y', end_date='today'),
            salary=fake.random_int(min=20000, max=150000)
        )
        self.employee2 = Employee.objects.create(
            name=fake.name(),
            position=fake.job_title(),
            office=fake.city(),
            age=fake.random_int(min=18, max=65),
            start_date=fake.date_between(start_date='-10y', end_date='today'),
            salary=fake.random_int(min=20000, max=150000)
        )

    # Rest of the test cases...
