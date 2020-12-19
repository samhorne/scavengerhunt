# Generated by Django 3.1.4 on 2020-12-19 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clues', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clue',
            name='codeword',
        ),
        migrations.AddField(
            model_name='clue',
            name='codeword_1',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='clue',
            name='codeword_2',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='clue',
            name='viewed_1',
            field=models.BooleanField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='clue',
            name='viewed_2',
            field=models.BooleanField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='clue',
            name='is_view',
            field=models.BooleanField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='clue',
            name='view',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
    ]
