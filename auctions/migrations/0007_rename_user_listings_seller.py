# Generated by Django 4.1 on 2022-08-30 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0006_listings_user"),
    ]

    operations = [
        migrations.RenameField(
            model_name="listings",
            old_name="user",
            new_name="seller",
        ),
    ]
