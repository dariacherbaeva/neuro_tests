from django import template

from med_tests.models import PatientProfile

register = template.Library()


@register.filter
def is_patient(user):
    return PatientProfile.objects.filter(user=user).exists()
