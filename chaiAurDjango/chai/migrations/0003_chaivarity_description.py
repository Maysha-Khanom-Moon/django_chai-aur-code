# Generated by Django 5.0.6 on 2024-06-17 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chai', '0002_rename_types_chaivarity_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='chaivarity',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
