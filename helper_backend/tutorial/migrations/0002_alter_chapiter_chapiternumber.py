# Generated by Django 4.2.4 on 2023-09-21 22:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapiter',
            name='chapiterNumber',
            field=models.CharField(default=uuid.UUID('54afca1f-ea50-4af9-a2b9-19dfda32b319'), editable=False, max_length=255),
        ),
    ]