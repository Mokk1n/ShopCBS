# Generated by Django 4.1.3 on 2022-12-06 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_alter_product_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='group',
            field=models.CharField(choices=[('notebook', 'notebook'), ('pc', 'pc'), ('mobile', 'mobile')], default='mobile', max_length=20),
        ),
    ]
