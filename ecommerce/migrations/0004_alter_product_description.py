# Generated by Django 5.0.2 on 2024-06-27 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0003_product_description_alter_orderitem_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=555, null=True),
        ),
    ]