# Generated by Django 2.2.2 on 2019-07-19 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receta', '0002_auto_20190719_1149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receta',
            name='NUR',
        ),
        migrations.AddField(
            model_name='receta',
            name='nur',
            field=models.CharField(default=1, max_length=255, verbose_name='NUR'),
            preserve_default=False,
        ),
    ]
