# Generated by Django 4.1.3 on 2022-11-11 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_alter_user_bio_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=10),
        ),
    ]
