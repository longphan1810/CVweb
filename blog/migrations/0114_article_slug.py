# Generated by Django 3.0.6 on 2020-09-14 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0113_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True),
        ),
    ]
