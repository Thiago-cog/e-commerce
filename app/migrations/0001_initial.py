# Generated by Django 4.1.2 on 2022-11-20 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('sobrenome', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('senha', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('preco', models.FloatField()),
                ('quantidade', models.BigIntegerField()),
                ('imagem', models.CharField(max_length=300)),
            ],
        ),
    ]
