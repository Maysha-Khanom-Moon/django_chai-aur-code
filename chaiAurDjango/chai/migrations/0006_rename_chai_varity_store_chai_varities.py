# Generated by Django 5.0.6 on 2024-06-17 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chai', '0005_chaicertificate_chaireview_store'),
    ]

    operations = [
        migrations.RenameField(
            model_name='store',
            old_name='chai_varity',
            new_name='chai_varities',
        ),
    ]