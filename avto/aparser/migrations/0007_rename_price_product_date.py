# Generated by Django 4.2 on 2023-04-26 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aparser', '0006_rename_productimport_avtoimport'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='date',
        ),
    ]