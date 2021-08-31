from datetime import datetime

from django.contrib.auth.models import User

from med_tests.models import QuestionnaireResponse, Questionnaire, MultipleChoiceQuestion, QuestionResponse, \
    ResponseOption, PatientProfile

DEPRESSION_ID = 2
SENSITIZATION_ID = 1


def count_points(result):
    points = 0
    for qr in result.question_responses.all():
        points += qr.response_option.cost
    result.points = points
    result.save()


def get_depression_test_results(result):
    count_points(result)
    # patient = PatientProfile.objects.get(user=result.user)
    # if 7 <= patient.age <= 12:
    #     if patient.gender == 'F':
    #         return


def get_sensitization_test_results(result):
    count_points(result)


# def get_response_option(request, )


def pass_test(request, test_id, user_id):
    questionnaire = Questionnaire.objects.get(id=test_id)
    questionnaire_response = QuestionnaireResponse.objects.create(questionnaire=questionnaire, user_id=user_id,
                                                                  timestamp=datetime.now())
    questions = MultipleChoiceQuestion.objects.filter(questionnaire=questionnaire)
    for question in questions:
        response_option_text = request.POST[f'{question.number}[]']
        response_option = ResponseOption.objects.get(question_id=question.id, text=response_option_text)
        question_response = QuestionResponse.objects.create(user_id=user_id, response_option=response_option)
        question_response.save()
        questionnaire_response.question_responses.add(question_response)

    if test_id == SENSITIZATION_ID:
        get_sensitization_test_results(questionnaire_response)
    if test_id == DEPRESSION_ID:
        get_depression_test_results(questionnaire_response)

    questionnaire_response.save()

    return questionnaire_response
