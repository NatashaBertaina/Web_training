# Generated by Django 5.0.4 on 2024-08-26 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainingApp', '0013_block_description_en_block_description_es_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='training',
            name='name_training_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='training',
            name='name_training_es',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
