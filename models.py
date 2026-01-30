from django.db import models


# Employee table
class Employee(models.Model):
    emp_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.emp_id


# Attendance log table (raw biometric punches)
class AttendanceLog(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.employee.emp_id} - {self.date} - {self.time}"
