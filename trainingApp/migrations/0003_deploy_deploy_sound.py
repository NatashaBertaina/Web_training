# Generated by Django 4.2.5 on 2023-09-27 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainingApp', '0002_deploy_deploy_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='deploy',
            name='deploy_sound',
            field=models.FileField(blank=True, null=True, upload_to='Deploy'),
        ),
    ]
