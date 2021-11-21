from datetime import datetime

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


# TODO: finish
def get_depression_test_results(result):
    count_points(result)
    patient = PatientProfile.objects.get(user=result.user)
    if 7 <= patient.age <= 12:
        if result.points == 0:
            if patient.gender == 'F':
                result.points = 37
            elif patient.gender == 'M':
                result.points = 35
        elif result.points == 1:
            if patient.gender == 'F':
                result.points = 39
            elif patient.gender == 'M':
                result.points = 37
        elif result.points == 2:
            if patient.gender == 'F':
                result.points = 40
            elif patient.gender == 'M':
                result.points = 38
        elif result.points == 3:
            if patient.gender == 'F':
                result.points = 42
            elif patient.gender == 'M':
                result.points = 39
        elif result.points == 4:
            if patient.gender == 'F':
                result.points = 43
            elif patient.gender == 'M':
                result.points = 41
        elif result.points == 5:
            if patient.gender == 'F':
                result.points = 44
            elif patient.gender == 'M':
                result.points = 42
        elif result.points == 6:
            if patient.gender == 'F':
                result.points = 46
            elif patient.gender == 'M':
                result.points = 44
        elif result.points == 7:
            if patient.gender == 'F':
                result.points = 47
            elif patient.gender == 'M':
                result.points = 45
        elif result.points == 8:
            if patient.gender == 'F':
                result.points = 49
            elif patient.gender == 'M':
                result.points = 46
        elif result.points == 9:
            if patient.gender == 'F':
                result.points = 48
            elif patient.gender == 'M':
                result.points = 50
        elif result.points == 10:
            result.points = 51
        elif result.points == 11:
            pass


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
