# Generated by Django 5.1.7 on 2025-04-07 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0013_post_intro_test'),
    ]

    operations = [
        migrations.DeleteModel(
            name='QuillPost',
        ),
        migrations.RemoveField(
            model_name='post',
            name='intro_test',
        ),
    ]
