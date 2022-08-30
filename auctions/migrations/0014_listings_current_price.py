# Generated by Django 4.1 on 2022-08-30 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0013_alter_listings_is_active"),
    ]

    operations = [
        migrations.AddField(
            model_name="listings",
            name="current_price",
            field=models.DecimalField(
                blank=True, decimal_places=2, default=1.01, max_digits=100
            ),
            preserve_default=False,
        ),
    ]
