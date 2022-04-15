# Generated by Django 2.2.16 on 2022-04-15 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_auto_20220415_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='genre',
            field=models.ManyToManyField(blank=True, db_index=True, related_name='Genre', to='reviews.Genre'),
        ),
    ]
