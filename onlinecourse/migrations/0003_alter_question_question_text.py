# Generated by Django 4.2.3 on 2023-07-13 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_rename_question_choice_question_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(default='Enter question here', max_length=200),
        ),
    ]