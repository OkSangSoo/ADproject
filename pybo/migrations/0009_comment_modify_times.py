# Generated by Django 3.1.3 on 2023-05-31 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0008_comment_voter'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='modify_times',
            field=models.IntegerField(default=0),
        ),
    ]
