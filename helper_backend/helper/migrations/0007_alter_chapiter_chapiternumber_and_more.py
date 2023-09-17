# Generated by Django 4.2.4 on 2023-09-17 14:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('helper', '0006_alter_chapiter_chapiternumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapiter',
            name='chapiterNumber',
            field=models.CharField(default=uuid.UUID('e93f8f29-77ab-4e8a-9643-025e85c0fa20'), editable=False, max_length=255),
        ),
        migrations.AlterField(
            model_name='chapiter',
            name='nextChapiter',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='nextChapiter'),
        ),
        migrations.AlterField(
            model_name='chapiter',
            name='previewChapiter',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='previewChapiter'),
        ),
    ]
