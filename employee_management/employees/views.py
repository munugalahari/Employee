from rest_framework import generics
from .models import Employee
from .serializers import EmployeeSerializer




class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


#to create more fake data use below code
# from faker import Faker
#
# fake = Faker()
#
#
# class EmployeeListCreateView(generics.ListCreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#
#     def perform_create(self, serializer):
#         serializer.save(
#             name=fake.name(),
#             position=fake.job(),
#             office=fake.city(),
#             age=fake.random_int(min=18, max=65),
#             start_date=fake.date_between(start_date='-10y', end_date='today'),
#             salary=fake.random_int(min=200000, max=1500000)
#         )
#
#
# class EmployeeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
