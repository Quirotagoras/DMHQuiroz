# Generated by Django 2.2.2 on 2019-06-26 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receta', '0007_auto_20190626_0101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receta',
            name='cbarras',
            field=models.CharField(max_length=100),
        ),
    ]
