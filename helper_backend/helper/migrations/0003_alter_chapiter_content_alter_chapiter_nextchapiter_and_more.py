# Generated by Django 4.2.4 on 2023-09-15 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helper', '0002_tutorialfield_chapiter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapiter',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='chapiter',
            name='nextChapiter',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='chapiter',
            name='previewChapiter',
            field=models.IntegerField(default=None),
        ),
    ]