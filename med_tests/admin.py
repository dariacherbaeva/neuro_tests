from django.contrib import admin

from med_tests.models import Questionnaire, MultipleChoiceQuestion, ResponseOption, QuestionResponse, \
    QuestionnaireResponse, QuestionnaireResponseMeaning, PatientProfile


class QuestionnaireAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


class MultipleChoiceQuestionAdmin(admin.ModelAdmin):
    list_display = ('number', 'text',)
    search_fields = ('text',)
    ordering = ('number', 'questionnaire')
    list_filter = ('questionnaire',)


class ResponseOptionAdmin(admin.ModelAdmin):
    list_display = ('text', 'cost',)
    search_fields = ('text',)
    ordering = ('question',)
    list_filter = ('question',)


class QuestionResponseAdmin(admin.ModelAdmin):
    list_display = ('response_option', 'user',)
    list_filter = ('user',)


class QuestionnaireResponseAdmin(admin.ModelAdmin):
    list_display = ('questionnaire', 'user', 'points',)
    list_filter = ('questionnaire', 'user')
    ordering = ('points',)
    search_fields = ('user', 'questionnaire')


class QuestionnaireResponseMeaningAdmin(admin.ModelAdmin):
    list_filter = ('questionnaire_response',)
    list_display = ('questionnaire_response', 'description')


class PatientProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'gender', 'age')
    list_filter = ('doctor', 'gender')
    ordering = ('age', 'user')


admin.site.register(Questionnaire, QuestionnaireAdmin)
admin.site.register(MultipleChoiceQuestion, MultipleChoiceQuestionAdmin)
admin.site.register(ResponseOption, ResponseOptionAdmin)
admin.site.register(QuestionResponse, QuestionResponseAdmin)
admin.site.register(QuestionnaireResponse, QuestionnaireResponseAdmin)
admin.site.register(QuestionnaireResponseMeaning, QuestionnaireResponseMeaningAdmin)
admin.site.register(PatientProfile, PatientProfileAdmin)
