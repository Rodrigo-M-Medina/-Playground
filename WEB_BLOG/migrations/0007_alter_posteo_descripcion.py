# Generated by Django 4.1.3 on 2022-12-27 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WEB_BLOG', '0006_alter_posteo_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posteo',
            name='descripcion',
            field=models.CharField(max_length=800),
        ),
    ]
