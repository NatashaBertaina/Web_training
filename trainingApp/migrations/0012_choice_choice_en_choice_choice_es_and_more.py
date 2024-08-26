# Generated by Django 5.0.4 on 2024-08-26 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainingApp', '0011_alter_block_state_block_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='choice_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='choice',
            name='choice_es',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='deploy',
            name='correct_answer_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='deploy',
            name='correct_answer_es',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='deploy',
            name='question_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='deploy',
            name='question_es',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='block',
            name='state_block',
            field=models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=20),
        ),
        migrations.AlterField(
            model_name='blockanswer',
            name='state_block',
            field=models.CharField(choices=[('In progress', 'In progress'), ('Completed', 'Completed')], default='In progress', max_length=20),
        ),
        migrations.AlterField(
            model_name='comment',
            name='least_liked',
            field=models.CharField(choices=[('Too difficult', 'Too difficult'), ('Not interesting', 'Not interesting'), ('Poorly explained', 'Poorly explained'), ('Confusing', 'Confusing'), ('Repetitive', 'Repetitive')], max_length=20),
        ),
        migrations.AlterField(
            model_name='comment',
            name='more_liked',
            field=models.CharField(choices=[('Well explained', 'Well explained'), ('Interesting', 'Interesting'), ('Easy to understand', 'Easy to understand')], max_length=20),
        ),
        migrations.AlterField(
            model_name='training',
            name='difficulty',
            field=models.CharField(choices=[('Easy', 'Easy'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')], default='Easy', max_length=20),
        ),
        migrations.AlterField(
            model_name='training',
            name='state_training',
            field=models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=20),
        ),
    ]
