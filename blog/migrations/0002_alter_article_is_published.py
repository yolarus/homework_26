# Generated by Django 5.1.3 on 2024-11-21 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Опубликовать'),
        ),
    ]
