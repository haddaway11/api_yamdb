# Generated by Django 2.2.16 on 2022-04-18 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0007_auto_20220418_1845'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={},
        ),
        migrations.RenameField(
            model_name='review',
            old_name='title_id',
            new_name='title',
        ),
    ]
