# Generated by Django 2.1.7 on 2019-03-15 04:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('largo_de_sepalo', models.FloatField()),
                ('ancho_de_sepalo', models.FloatField()),
                ('largo_de_petalo', models.FloatField()),
                ('ancho_de_petalo', models.FloatField()),
                ('prediccion', models.IntegerField()),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
