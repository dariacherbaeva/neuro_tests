from django.template.defaultfilters import register

from med_tests.models import PatientProfile


@register.filter
def is_patient(request):
    return PatientProfile.objects.filter(user=request.user).exists()
