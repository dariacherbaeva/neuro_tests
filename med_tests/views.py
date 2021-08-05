from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import TemplateView

from med_tests.models import QuestionnaireResponse, Questionnaire, MultipleChoiceQuestion

DEPRESSION_ID = 2
SENSITIZATION_ID = 1


class PassDepressionTest(LoginRequiredMixin, TemplateView):

    template_name = 'depression_test.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['questionnaire'] = Questionnaire.objects.get(id=DEPRESSION_ID)
        context['questions'] = MultipleChoiceQuestion.objects.filter(questionnaire_id=DEPRESSION_ID)
        return context

class PassSensitizationTest(LoginRequiredMixin, TemplateView):

    template_name = 'sensitization_test.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['questionnaire'] = Questionnaire.objects.get(id=SENSITIZATION_ID)
        context['questions'] = MultipleChoiceQuestion.objects.filter(questionnaire_id=SENSITIZATION_ID)
        return context


