# Generated by Django 2.2.2 on 2019-06-26 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equivalencia', '0002_auto_20190626_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equivalencia',
            name='descripcion_equivalente',
            field=models.CharField(max_length=200),
        ),
    ]