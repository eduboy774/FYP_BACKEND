# Generated by Django 3.0 on 2022-04-29 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD_backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='appointment_description',
            field=models.CharField(default='no comment', max_length=200),
            preserve_default=False,
        ),
    ]
