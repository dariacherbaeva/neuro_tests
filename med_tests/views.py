from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.views import View
from django.views.generic import TemplateView, FormView

from med_tests.models import Questionnaire, MultipleChoiceQuestion, QuestionResponse, ResponseOption, \
    QuestionnaireResponse, PatientProfile
from med_tests.utils import pass_test, get_sensitization_test_results, get_depression_test_results

DEPRESSION_ID = 2
SENSITIZATION_ID = 1


class ShowTest(LoginRequiredMixin, TemplateView):
    template_name = 'test_page.html'

    @property
    def test_id(self):
        return self.kwargs['test_id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['questionnaire'] = Questionnaire.objects.get(id=self.test_id)
        context['questions'] = MultipleChoiceQuestion.objects.filter(questionnaire_id=self.test_id)
        return context


class PassTest(LoginRequiredMixin, TemplateView):
    template_name = 'success.html'

    @property
    def test_id(self):
        return self.kwargs['test_id']

    def post(self, request, **kwargs):
        context = self.get_context_data(**kwargs)
        questionnaire = Questionnaire.objects.get(id=self.test_id)
        questionnaire_response = pass_test(request, self.test_id, request.user.id)
        context['questionnaire_response'] = questionnaire_response
        return self.render_to_response(context)


class ProfilePage(LoginRequiredMixin, TemplateView):
    template_name = "profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        patient = PatientProfile.objects.filter(user=self.request.user)
        if patient:
            context['patient'] = patient.first()
        return context
