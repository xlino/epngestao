# Generated by Django 4.0.1 on 2022-04-07 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle', '0002_alter_customer_email_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pendente', 'Pendente'), ('Atrasada', 'Atrasada'), ('Entregue', 'Entregue'), ('Suspensa', 'Suspensa')], max_length=200, null=True),
        ),
    ]
