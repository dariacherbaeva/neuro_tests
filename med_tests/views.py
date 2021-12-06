from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, FormView

from med_tests.forms import QuestionnairePrescriptionForm
from med_tests.models import Questionnaire, MultipleChoiceQuestion, QuestionResponse, ResponseOption, \
    QuestionnaireResponse, PatientProfile, QuestionnairePrescription
from med_tests.utils import pass_test, get_sensitization_test_results, get_depression_test_results

DEPRESSION_ID = 2
SENSITIZATION_ID = 1


class ShowTest(LoginRequiredMixin, TemplateView):
    template_name = 'tests/test_page.html'

    @property
    def test_id(self):
        return self.kwargs['test_id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['questionnaire'] = Questionnaire.objects.get(id=self.test_id)
        context['questions'] = MultipleChoiceQuestion.objects.filter(questionnaire_id=self.test_id)
        return context


class PassTest(LoginRequiredMixin, View):

    @property
    def test_id(self):
        return self.kwargs['test_id']

    def post(self, request, **kwargs):
        prescription = QuestionnairePrescription.objects.get(patient=request.user,
                                                             questionnaire_id=self.test_id,
                                                             is_finished=False)
        if prescription:
            prescription.result = pass_test(request, self.test_id, request.user.id)
            prescription.save()
        else:
            redirect(reverse_lazy('tests'))
        return redirect(reverse_lazy('my_profile'))


class ProfilePage(LoginRequiredMixin, TemplateView):
    template_name = "patients/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'user_id' in self.kwargs.keys():
            context['user'] = User.objects.get(id=self.kwargs['user_id'])
            patient = PatientProfile.objects.filter(user_id=self.kwargs['user_id'])
        else:
            context['user'] = User.objects.get(id=self.request.user.id)
            patient = PatientProfile.objects.filter(user_id=self.request.user)
        if patient:
            context['patient'] = patient.first()
        return context


class TestList(LoginRequiredMixin, TemplateView):
    template_name = "tests/test_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        patient = PatientProfile.objects.get(user=self.request.user)
        if patient:
            context['patient'] = patient
        context['tests'] = patient.get_patient_prescriptions()
        return context


class PatientList(LoginRequiredMixin, TemplateView):
    template_name = "patients/patient_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        patient = PatientProfile.objects.filter(user=self.request.user)
        if not patient:
            patients = PatientProfile.objects.filter(doctor=self.request.user)
            context['patients'] = patients
        return context


class HomePageView(View):

    def get(self, request):
        if self.request.user:
            return redirect(reverse_lazy('my_profile'))
        else:
            return redirect(reverse_lazy('login'))


class CreateQuestionnairePrescription(LoginRequiredMixin, FormView):
    template_name = 'doctor/create_prescription.html'
    form_class = QuestionnairePrescriptionForm

    def get_success_url(self):
        return reverse_lazy('prescribe_test')

    def form_valid(self, form):
        form.save()
        return super(CreateQuestionnairePrescription, self).form_valid(form)

