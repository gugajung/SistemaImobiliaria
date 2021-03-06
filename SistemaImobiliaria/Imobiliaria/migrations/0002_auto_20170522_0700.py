# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-22 07:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Imobiliaria', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empreendimento',
            name='video',
            field=models.URLField(blank=True, null=True, verbose_name='Vídeo no Youtube'),
        ),
        migrations.AlterField(
            model_name='estabelecimentocomercial',
            name='acesso',
            field=models.CharField(blank=True, choices=[('TR', 'Térreo'), ('1S', '1° Sobreloja'), ('2S', '2° Sobreloja'), ('3S', '3° Sobreloja')], max_length=100, null=True, verbose_name='Acesso'),
        ),
        migrations.AlterField(
            model_name='estabelecimentocomercial',
            name='locatario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Imobiliaria.Pessoa', verbose_name='Morador Locatário'),
        ),
        migrations.AlterField(
            model_name='estabelecimentocomercial',
            name='tipo',
            field=models.CharField(blank=True, choices=[('PC', 'Ponto Comercial'), ('AC', 'Academia'), ('AÇ', 'Açougue'), ('AF', 'Artigos de Feta'), ('AT', 'Atacado'), ('AV', 'Avícola'), ('AC', 'Avicultura'), ('BJ', 'Banca de Jornal'), ('BR', 'Bar'), ('BP', 'Bazar e Papelaria'), ('Bo', 'Boate'), ('BM', 'Bom Boniere'), ('BF', 'Buffet'), ('CB', 'Cabelereiro'), ('CE', 'Café Expresso'), ('CS', 'Cantina de Escola'), ('CC', 'Casa Comercial'), ('CS', 'Casa de Sucos'), ('CT', 'Centro Automotivo'), ('CP', 'Copiadora'), ('CZ', 'Cozinha Industrial'), ('DP', 'Depósito'), ('DG', 'Depósito de gás'), ('DK', 'Disk Água'), ('DP', 'Disk Pizza'), ('DC', 'Doceria'), ('EM', 'Embalagens'), ('ES', 'Escola'), ('EF', 'Esfilharia'), ('ET', 'Estacionamento'), ('FB', 'Aábrica'), ('FM', 'Farmácia'), ('GL', 'Gelaria'), ('GP', 'Galpão'), ('HT', 'Hotel'), ('ID', 'Indústria'), ('LH', 'Lan House'), ('LC', 'Lanchonet'), ('LR', 'Lava Rápido'), ('LR', 'Locação de Roupas'), ('LC', 'Loja de Calçados'), ('LF', 'Loja de Ferragens'), ('LF', 'Loja de Fraudas'), ('LL', 'Loja de Langerie'), ('LR', 'Loja de Roupas'), ('LU', 'Loja de Utilidades'), ('LT', 'Lotérica'), ('MC', 'Mercado'), ('MT', 'Motel'), ('PD', 'Padria'), ('PP', 'Papelaria'), ('PS', 'Pastelaria'), ('PF', 'Perfumaria'), ('PS', 'Pet Shop'), ('PZ', 'Pizzaria'), ('PG', 'Posto de Gasolina'), ('PU', 'Pousada'), ('PC', 'Prédio Comercial'), ('PL', 'Produtos de Limpeza'), ('QU', 'Quitanda'), ('RT', 'Restaurante'), ('RF', 'Retífica'), ('RV', 'Revistaria'), ('RS', 'Rotisserie'), ('SC', 'Salão Comercial'), ('SP', 'Shoping Center'), ('SM', 'Supermercado'), ('VL', 'Video Locadora'), ('CL', 'Clínica')], max_length=100, null=True, verbose_name='Tipo'),
        ),
        migrations.AlterField(
            model_name='fisica',
            name='rg',
            field=models.PositiveIntegerField(blank=True, help_text='Somente Números', max_length=30, null=True, verbose_name='RG'),
        ),
        migrations.AlterField(
            model_name='visita',
            name='data',
            field=models.DateField(default=datetime.datetime(2017, 5, 22, 7, 0, 24, 836720), help_text='dd/mm/aaa', verbose_name='Data'),
        ),
    ]
