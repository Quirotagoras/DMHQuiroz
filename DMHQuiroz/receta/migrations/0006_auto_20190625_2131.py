# Generated by Django 2.2.2 on 2019-06-25 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('receta', '0005_auto_20190625_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receta',
            name='equivalencia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='equivalencia.Equivalencia'),
        ),
    ]
