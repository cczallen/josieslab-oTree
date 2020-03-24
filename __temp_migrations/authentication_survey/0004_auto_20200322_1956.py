# Generated by Django 2.2.4 on 2020-03-22 11:56

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication_survey', '0003_remove_player_testq_passed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='testQ',
        ),
        migrations.AddField(
            model_name='player',
            name='authentication_question_passed',
            field=otree.db.models.StringField(choices=[[False, '1'], [False, '26'], [True, '56'], [False, '64']], max_length=10000, null=True, verbose_name='驗證問題：請回答 30 x 2 - 4 = ?'),
        ),
    ]