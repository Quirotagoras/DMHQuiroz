# Generated by Django 2.2.2 on 2019-08-27 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('farmacia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('last_name', models.CharField(max_length=50, verbose_name='Apellido Paterno')),
                ('last_name2', models.CharField(max_length=50, verbose_name='Apellido Materno')),
                ('cedula', models.CharField(max_length=50, verbose_name='Cedula Profesional')),
                ('telefono', models.BigIntegerField()),
                ('calle_num', models.CharField(max_length=100, verbose_name='Calle y numero')),
                ('estado', models.CharField(choices=[('AGS', 'Aguascalientes'), ('BC', 'Baja California'), ('BCS', 'Baja California Sur'), ('CAMP', 'Campeche'), ('CHIA', 'Chiapas'), ('CHIH', 'Chihuahua'), ('COA', 'Coahuila'), ('COL', 'Colima'), ('DUR', 'Durango'), ('EDOMEX', 'Estado de Mexico'), ('GTO', 'Guanajuato'), ('GRRO', 'Guerrero'), ('HGO', 'Hidalgo'), ('JAL', 'Jalisco'), ('MICH', 'Michoacan'), ('MOR', 'Morelos'), ('NAY', 'Nayarit'), ('NL', 'Nuevo Leon'), ('OAX', 'Oaxaca'), ('PUE', 'Puebla'), ('QRO', 'Queretaro'), ('QUROO', 'Quintana Roo'), ('SLP', 'San Luis Potosi'), ('SIN', 'Sinaloa'), ('SON', 'Sonora'), ('TAB', 'Tabasco'), ('TAM', 'Tamaulipas'), ('TLAX', 'Tlaxcala'), ('VER', 'Veracruz'), ('YUC', 'Yucatan'), ('ZAC', 'Zacatecas')], max_length=100)),
                ('municipio', models.CharField(max_length=100)),
                ('cp', models.CharField(max_length=10, verbose_name='Codigo Postal')),
                ('farmacia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmacia.Farmacia')),
            ],
        ),
    ]
