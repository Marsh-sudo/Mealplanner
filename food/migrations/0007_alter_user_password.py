# Generated by Django 4.1.3 on 2022-11-12 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0006_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=150),
        ),
    ]
