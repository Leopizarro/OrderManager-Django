# Generated by Django 3.1.7 on 2021-03-16 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motoristas', '0002_motorista_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='motorista',
            name='zona',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
