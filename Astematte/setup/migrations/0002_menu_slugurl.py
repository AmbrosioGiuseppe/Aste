# Generated by Django 4.1.3 on 2022-12-28 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='slugUrl',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]