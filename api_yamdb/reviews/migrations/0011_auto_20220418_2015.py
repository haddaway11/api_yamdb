# Generated by Django 2.2.16 on 2022-04-18 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0010_auto_20220418_2005'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='review',
            name='qwe',
        ),
        migrations.AddConstraint(
            model_name='review',
            constraint=models.UniqueConstraint(fields=('title', 'author'), name='title_author'),
        ),
    ]
