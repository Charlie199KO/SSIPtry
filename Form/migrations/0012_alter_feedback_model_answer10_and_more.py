# Generated by Django 4.2.6 on 2023-11-03 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Form', '0011_alter_feedback_model_overall_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback_model',
            name='answer10',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='feedback_model',
            name='answer3',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='feedback_model',
            name='answer6',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='feedback_model',
            name='answer7',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='feedback_model',
            name='answer8',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='feedback_model',
            name='answer9',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='feedback_model',
            name='overall_rating',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
