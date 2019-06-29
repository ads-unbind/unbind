# Generated by Django 2.2.2 on 2019-06-29 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atividade', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='atividade',
            name='imagem',
            field=models.ImageField(blank=True, upload_to='imagem_atividade'),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='descricao',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='titulo',
            field=models.CharField(max_length=30),
        ),
    ]