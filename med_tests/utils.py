from med_tests.models import QuestionnaireResponse


def get_depression_test_results(user):
    result = QuestionnaireResponse.objects.filter(user=user).order_by('timestamp').first()
    # TODO add age and gender to user model
