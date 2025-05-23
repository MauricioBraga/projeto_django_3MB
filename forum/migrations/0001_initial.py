# Generated by Django 3.2.25 on 2025-04-25 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pergunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('detalhe', models.TextField()),
                ('tentativa', models.TextField()),
                ('data_criacao', models.DateTimeField(verbose_name='Criado em ')),
                ('usuario', models.CharField(default='anônimo', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Resposta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField()),
                ('votos', models.IntegerField(default=0)),
                ('data_criacao', models.DateTimeField(verbose_name='Criado em ')),
                ('usuario', models.CharField(default='anônimo', max_length=200)),
                ('pergunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.pergunta')),
            ],
        ),
    ]
