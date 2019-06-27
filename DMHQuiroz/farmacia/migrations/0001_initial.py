# Generated by Django 2.2.2 on 2019-06-27 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Farmacia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cve_admin', models.IntegerField(unique=True, verbose_name='Clave de administrador')),
                ('cve_admin2', models.CharField(max_length=50, unique=True, verbose_name='Clave de administrador 2')),
                ('nombre', models.CharField(max_length=50)),
                ('telefono', models.BigIntegerField(verbose_name='Telefono de farmacia')),
                ('calle_num', models.CharField(max_length=100, verbose_name='Calle y numero')),
                ('estado', models.CharField(choices=[('AGS', 'Aguascalientes'), ('BC', 'Baja California'), ('BCS', 'Baja California Sur'), ('CAMP', 'Campeche'), ('CHIA', 'Chiapas'), ('CHIH', 'Chihuahua'), ('COA', 'Coahuila'), ('COL', 'Colima'), ('DUR', 'Durango'), ('EDOMEX', 'Estado de Mexico'), ('GTO', 'Guanajuato'), ('GRRO', 'Guerrero'), ('HGO', 'Hidalgo'), ('JAL', 'Jalisco'), ('MICH', 'Michoacan'), ('MOR', 'Morelos'), ('NAY', 'Nayarit'), ('NL', 'Nuevo Leon'), ('OAX', 'Oaxaca'), ('PUE', 'Puebla'), ('QRO', 'Queretaro'), ('QUROO', 'Quintana Roo'), ('SLP', 'San Luis Potosi'), ('SIN', 'Sinaloa'), ('SON', 'Sonora'), ('TAB', 'Tabasco'), ('TAM', 'Tamaulipas'), ('TLAX', 'Tlaxcala'), ('VER', 'Veracruz'), ('YUC', 'Yucatan'), ('ZAC', 'Zacatecas')], max_length=15)),
                ('municipio', models.CharField(max_length=100)),
                ('cp', models.PositiveIntegerField(verbose_name='Codigo Postal')),
            ],
        ),
    ]
