# Generated by Django 2.2.2 on 2019-06-14 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20190614_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='capturista',
            name='email',
            field=models.EmailField(default='a@gmail.com', max_length=254),
            preserve_default=False,
        ),
    ]