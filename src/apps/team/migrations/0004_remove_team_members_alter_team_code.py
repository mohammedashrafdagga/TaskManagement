# Generated by Django 4.1.7 on 2023-03-14 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("team", "0003_alter_team_code"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="team",
            name="members",
        ),
        migrations.AlterField(
            model_name="team",
            name="code",
            field=models.CharField(default="dktnev", max_length=6),
        ),
    ]
