# Generated by Django 4.2.4 on 2023-09-15 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helper', '0004_alter_chapiter_nextchapiter_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapiter',
            name='nextChapiter',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='chapiter',
            name='previewChapiter',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
