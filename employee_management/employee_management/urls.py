from django.urls import path
from employees.views import EmployeeListCreateView, EmployeeRetrieveUpdateDestroyView

urlpatterns = [
    path('api/employees/', EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('api/employees/<int:pk>/', EmployeeRetrieveUpdateDestroyView.as_view(), name='employee-retrieve-update-destroy'),
]
