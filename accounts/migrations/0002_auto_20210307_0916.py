# Generated by Django 3.1.7 on 2021-03-07 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.TextField(blank=True, max_length=55, null=True),
        ),
        migrations.DeleteModel(
            name='City',
        ),
    ]