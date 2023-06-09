# Generated by Django 4.2 on 2023-04-26 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aparser', '0004_alter_product_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productimport',
            old_name='CSV',
            new_name='csv_file',
        ),
        migrations.AlterField(
            model_name='product',
            name='link_car',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=150),
        ),
    ]
