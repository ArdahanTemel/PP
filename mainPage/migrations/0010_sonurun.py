# Generated by Django 4.2.2 on 2023-08-01 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainPage", "0009_alter_kantar_note"),
    ]

    operations = [
        migrations.CreateModel(
            name="SonUrun",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("urun", models.CharField(max_length=200, verbose_name="Ürün Tipi")),
            ],
        ),
    ]
