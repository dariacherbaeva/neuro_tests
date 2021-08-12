from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


class Questionnaire(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()

    # questions = models.ManyToManyField('MultipleChoiceQuestion', on_delete=models.CASCADE)
    # TODO add max points (?)

    def __str__(self):
        return self.name


class MultipleChoiceQuestion(models.Model):
    number = models.IntegerField()
    text = models.TextField(blank=True, null=True)
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['number', 'questionnaire'], ['text', 'questionnaire']]

    def __str__(self):
        if self.text:
            return '%s %s %s' % (self.number, self.text, self.questionnaire.name)
        else:
            return '%s %s' % (self.number, self.questionnaire.name)

    def get_response_options(self):
        response_options = ResponseOption.objects.filter(question=self)
        return response_options


class ResponseOption(models.Model):
    text = models.TextField()
    cost = models.IntegerField()
    question = models.ForeignKey(MultipleChoiceQuestion, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s %s' % (self.text, str(self.question.number), self.question.questionnaire.name)


class QuestionResponse(models.Model):
    response_option = models.ForeignKey(ResponseOption, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.response_option.text, self.user.username)


class QuestionnaireResponse(models.Model):
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question_responses = models.ManyToManyField(QuestionResponse)
    points = models.IntegerField(default=0)
    timestamp = models.DateField(default=now, editable=False)

    def __str__(self):
        return '%s %s' % (self.questionnaire.name, self.user.username)


class PatientProfile(models.Model):
    GENDER_CHOICES = [
        ('M', "male"),
        ('F', 'female')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    age = models.IntegerField()
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctor')


class QuestionnaireResponseMeaning(models.Model):
    questionnaire_response = models.ForeignKey(QuestionnaireResponse, on_delete=models.CASCADE)
    description = models.TextField()
