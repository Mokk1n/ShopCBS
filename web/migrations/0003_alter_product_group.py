# Generated by Django 4.1.3 on 2022-12-05 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_alter_product_group_alter_product_img_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='group',
            field=models.CharField(choices=[('notebook', 'notebook'), ('mobile', 'mobile'), ('pc', 'pc')], default='mobile', max_length=20),
        ),
    ]
