# Generated by Django 2.2.4 on 2020-03-29 09:15

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('rounds_test', '0015_auto_20200329_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='get_money_now_or_future',
            field=otree.db.models.BooleanField(choices=[(True, True), (False, False)], null=True, verbose_name='請選擇您要今天或未來的報酬'),
        ),
    ]
