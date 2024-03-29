# Generated by Django 5.0.2 on 2024-02-23 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0004_product_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="thumbnail",
            field=models.ImageField(
                blank=True, null=True, upload_to="uploads/product_images/thumbnail/"
            ),
        ),
    ]
