# Generated by Django 4.0.3 on 2022-04-07 01:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Farmacia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('razao_sicial', models.CharField(max_length=60)),
                ('cnpj', models.CharField(max_length=18)),
                ('whatsapp', models.CharField(max_length=14)),
                ('telefone', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=254)),
                ('plantonista', models.BooleanField()),
                ('url_image', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='EscalaPlantao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia_hora_inicio', models.DateTimeField()),
                ('dia_hora_fechamento', models.DateTimeField()),
                ('farmacia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='escalaPlantao', to='encontraFarma.farmacia')),
            ],
        ),
        migrations.CreateModel(
            name='DiasHorarioFuncionamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia_semana', models.CharField(choices=[('SEG', 'SEGUNDA-FEIRA'), ('TER', 'TERÇA-FEIRA'), ('QUA', 'QUARTA-FEIRA'), ('QUI', 'QUINTA-FEIRA'), ('FEI', 'FEIRA-FEIRA'), ('SAB', 'SABADO-FEIRA'), ('DOM', 'DOMINGO-FEIRA')], max_length=3, unique=True)),
                ('hora_inicio', models.TimeField()),
                ('hora_fechamento', models.TimeField()),
                ('farmacia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diasHorarioFuncionamento', to='encontraFarma.farmacia')),
            ],
        ),
    ]
