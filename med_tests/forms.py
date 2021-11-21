from django.forms import ModelForm

from med_tests.models import QuestionnairePrescription


class QuestionnairePrescriptionForm(ModelForm):
    class Meta:
        model = QuestionnairePrescription
        fields = ['questionnaire', 'patient']
