# Generated by Django 2.2.2 on 2019-07-19 15:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('equivalencia', '0001_initial'),
        ('farmacia', '0001_initial'),
        ('derechohabiente', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NUR', models.CharField(max_length=255, verbose_name='NUR')),
                ('folio_receta', models.CharField(max_length=255, verbose_name='Folio de Receta')),
                ('status', models.CharField(max_length=100)),
                ('fecha_expide', models.DateTimeField(verbose_name='Fecha de expedicion')),
                ('fecha_recibe', models.DateTimeField(verbose_name='Fecha que recibe')),
                ('fecha_surte', models.DateTimeField(verbose_name='Fecha que surte')),
                ('doctor', models.CharField(max_length=100)),
                ('cantidad', models.IntegerField()),
                ('equivalencia_obs', models.TextField(blank=True, max_length=300, null=True)),
                ('creado', models.DateTimeField()),
                ('ultimamodif', models.DateTimeField()),
                ('has_Equivalencia', models.BooleanField(default=False)),
                ('cbarras', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('equivalencia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='equivalencia.Equivalencia')),
                ('farmacia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmacia.Farmacia')),
                ('ficha_derechohabiente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='derechohabiente.DerechoHabiente')),
            ],
        ),
    ]
