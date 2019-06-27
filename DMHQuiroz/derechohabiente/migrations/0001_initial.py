# Generated by Django 2.2.2 on 2019-06-27 21:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('farmacia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DerechoHabiente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ficha', models.PositiveIntegerField()),
                ('codigo', models.PositiveIntegerField()),
                ('org', models.CharField(blank=True, max_length=50, null=True)),
                ('nombre', models.CharField(max_length=50)),
                ('calle_num', models.CharField(max_length=100, verbose_name='Calle y numero')),
                ('colonia', models.CharField(max_length=100)),
                ('estado', models.CharField(choices=[('AGS', 'Aguascalientes'), ('BC', 'Baja California'), ('BCS', 'Baja California Sur'), ('CAMP', 'Campeche'), ('CHIA', 'Chiapas'), ('CHIH', 'Chihuahua'), ('COA', 'Coahuila'), ('COL', 'Colima'), ('DUR', 'Durango'), ('EDOMEX', 'Estado de Mexico'), ('GTO', 'Guanajuato'), ('GRRO', 'Guerrero'), ('HGO', 'Hidalgo'), ('JAL', 'Jalisco'), ('MICH', 'Michoacan'), ('MOR', 'Morelos'), ('NAY', 'Nayarit'), ('NL', 'Nuevo Leon'), ('OAX', 'Oaxaca'), ('PUE', 'Puebla'), ('QRO', 'Queretaro'), ('QUROO', 'Quintana Roo'), ('SLP', 'San Luis Potosi'), ('SIN', 'Sinaloa'), ('SON', 'Sonora'), ('TAB', 'Tabasco'), ('TAM', 'Tamaulipas'), ('TLAX', 'Tlaxcala'), ('VER', 'Veracruz'), ('YUC', 'Yucatan'), ('ZAC', 'Zacatecas')], max_length=100)),
                ('municipio', models.CharField(max_length=50)),
                ('cp', models.PositiveIntegerField(verbose_name='Codigo postal')),
                ('telefono', models.BigIntegerField()),
                ('email', models.EmailField(max_length=50)),
                ('farmacia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmacia.Farmacia')),
            ],
        ),
    ]
