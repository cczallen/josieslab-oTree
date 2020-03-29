# Generated by Django 2.2.4 on 2020-03-29 19:53

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('rounds_test', '0022_auto_20200330_0338'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='treatment_subject_included',
            field=otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, null=True),
        ),
    ]
