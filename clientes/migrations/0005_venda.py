# Generated by Django 4.0.1 on 2022-02-10 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0004_documento_person_doc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=7)),
                ('valor', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('desconto', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('impostos', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('pessoa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='clientes.person')),
            ],
        ),
    ]
