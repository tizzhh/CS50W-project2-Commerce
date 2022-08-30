# Generated by Django 4.1 on 2022-08-30 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0004_alter_user_watchlist"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="watchlist",
            field=models.ManyToManyField(
                blank=True, related_name="watchlist", to="auctions.listings"
            ),
        ),
    ]
