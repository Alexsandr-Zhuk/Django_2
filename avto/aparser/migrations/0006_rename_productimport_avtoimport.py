# Generated by Django 4.2 on 2023-04-26 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aparser', '0005_rename_csv_productimport_csv_file_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductImport',
            new_name='AvtoImport',
        ),
    ]
