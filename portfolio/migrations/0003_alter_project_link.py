# Generated by Django 5.1.5 on 2025-01-30 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_alter_project_options_project_link_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='link',
            field=models.URLField(blank=True, null=True, verbose_name='Dirección Web'),
        ),
    ]
