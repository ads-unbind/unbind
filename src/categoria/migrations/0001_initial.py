# Generated by Django 2.0.7 on 2019-05-14 02:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('questionario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('questionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questionario.Questionario')),
            ],
        ),
    ]