from django.core.validators import RegexValidator
from django.db import models


phone_regex = RegexValidator(
    regex=r'^\+998\d{9}$',
    message="Phone number must be entered in the format: '+998xxxxxxxxx'. Up to 9 digits allowed."
)


class Employee(models.Model):
    full_name = models.CharField(max_length=150, null=False, blank=False)
    phone_number = models.CharField(max_length=15, unique=True, validators=[phone_regex], null=True)

    email = models.EmailField(max_length=50, unique=True, null=True)
    job_title = models.CharField(max_length=150, blank=False, null=False)

    salary = models.DecimalField(max_digits=15, decimal_places=2)
    hire_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ['-created_at']