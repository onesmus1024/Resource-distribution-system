# Generated by Django 4.0.2 on 2022-05-23 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('government', '0004_consumer_product_name_alter_importer_amount_bought_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='localsupplier',
            name='date_of_delivery',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]