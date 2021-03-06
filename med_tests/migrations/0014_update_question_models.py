# Generated by Django 3.2.5 on 2022-03-23 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('med_tests', '0013_add_doctor_patient_connection_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='multiplechoicequestion',
            name='type',
            field=models.CharField(choices=[('t', 'text'), ('o', 'options')], default='o', max_length=1),
        ),
        migrations.CreateModel(
            name='TextQuestionResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response_text', models.TextField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='med_tests.multiplechoicequestion')),
            ],
        ),
    ]
