# Generated by Django 5.0.6 on 2024-06-17 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chai', '0003_chaivarity_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='chaivarity',
            name='price',
            field=models.TextField(default=''),
        ),
    ]
