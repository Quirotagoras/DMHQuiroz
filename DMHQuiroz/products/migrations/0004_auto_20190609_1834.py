# Generated by Django 2.2.2 on 2019-06-09 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20190609_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cbarras',
            field=models.IntegerField(),
        ),
    ]
