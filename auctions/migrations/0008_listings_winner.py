# Generated by Django 4.1 on 2022-08-30 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0007_rename_user_listings_seller"),
    ]

    operations = [
        migrations.AddField(
            model_name="listings",
            name="winner",
            field=models.CharField(blank=True, max_length=64),
        ),
    ]
