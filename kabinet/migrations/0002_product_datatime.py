# Generated by Django 4.0.6 on 2022-10-11 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kabinet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='datatime',
            field=models.DateTimeField(default=1),
            preserve_default=False,
        ),
    ]
