from django import template

from med_tests.models import PatientProfile

register = template.Library()


@register.filter
def is_patient(request):
    return PatientProfile.objects.filter(user=request.user).exists()
