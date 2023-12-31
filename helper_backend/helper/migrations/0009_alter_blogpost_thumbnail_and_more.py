# Generated by Django 4.2.4 on 2023-09-19 08:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('helper', '0008_blogpost_alter_chapiter_chapiternumber_postcontent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='thumbnail',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='thumbnail'),
        ),
        migrations.AlterField(
            model_name='chapiter',
            name='chapiterNumber',
            field=models.CharField(default=uuid.UUID('c475ec5b-643f-4ddb-bb27-716a11d8b959'), editable=False, max_length=255),
        ),
        migrations.AlterField(
            model_name='chapiter',
            name='thumbnail',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='thumbnail'),
        ),
        migrations.AlterField(
            model_name='tutorialfield',
            name='thumbnail',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='thumbnail'),
        ),
    ]
