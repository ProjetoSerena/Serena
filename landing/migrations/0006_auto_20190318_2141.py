# Generated by Django 2.1.7 on 2019-03-19 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0005_auto_20190317_1634'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cadastro',
            name='email_emergencia2',
        ),
        migrations.RemoveField(
            model_name='cadastro',
            name='nome_emergencia2',
        ),
        migrations.RemoveField(
            model_name='cadastro',
            name='tel_emergencia2',
        ),
        migrations.AddField(
            model_name='cadastro',
            name='grau_parentesco',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='celular',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='username',
            field=models.CharField(max_length=30, verbose_name='User'),
        ),
    ]
