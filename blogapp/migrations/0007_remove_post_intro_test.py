# Generated by Django 5.1.7 on 2025-04-05 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0006_post_intro_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='intro_test',
        ),
    ]
