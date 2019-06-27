# Generated by Django 2.2.2 on 2019-06-27 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cbarras', models.BigIntegerField(unique=True, verbose_name='Codgio de Barras')),
                ('ubicacion', models.CharField(max_length=100)),
                ('nombre_activo', models.CharField(max_length=200)),
                ('nombre_comercial', models.CharField(max_length=200)),
                ('presentacion', models.CharField(max_length=200)),
                ('empaque', models.CharField(max_length=50)),
                ('dcantidad', models.PositiveIntegerField()),
                ('unidad_medida', models.CharField(choices=[('mg', 'miligramos'), ('g', 'gramos'), ('ml', 'mililitros')], max_length=20, verbose_name='Unidad de medida')),
                ('presenta', models.CharField(choices=[('Tabletas', 'Tabletas'), ('Amp', 'Ampolletas'), ('Polv', 'Polvos'), ('Cap', 'Capsulas'), ('Pil', 'Pildoras'), ('Grag', 'Grageas'), ('Sup', 'Supositorios'), ('Ov', 'Ovulos'), ('Pom', 'Pomada'), ('Cre', 'Crema'), ('Sol', 'Soluciones'), ('Jar', 'Jarabes'), ('Col', 'Colirios'), ('Loc', 'Lociones'), ('Lin', 'Linimiento'), ('Eli', 'Elixir'), ('Ene', 'Enema'), ('Inha', 'Inhalaciones'), ('Aero', 'Aerosoles')], max_length=100)),
                ('gramaje', models.CharField(max_length=10)),
                ('cve_farmacia', models.IntegerField()),
                ('costo_venta', models.FloatField()),
                ('costo_compra', models.FloatField()),
                ('iva', models.IntegerField()),
                ('proveedor', models.CharField(max_length=20)),
                ('stock', models.IntegerField()),
                ('modificacion', models.CharField(max_length=3)),
                ('registro', models.CharField(max_length=20)),
                ('grupo', models.CharField(max_length=2)),
                ('laboratorio', models.CharField(max_length=20)),
                ('pais', models.CharField(max_length=20)),
                ('tlc', models.CharField(max_length=3)),
                ('pumpvp', models.FloatField()),
                ('modalidad_real', models.CharField(max_length=2)),
            ],
        ),
    ]
