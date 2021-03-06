# Generated by Django 3.2.5 on 2021-08-12 20:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('med_tests', '0006_add_patient_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionnaireResponseMeaning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('questionnaire_response', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='med_tests.questionnaireresponse')),
            ],
        ),
    ]
