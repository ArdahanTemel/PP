# Generated by Django 4.2.2 on 2023-08-14 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainPage", "0013_alter_malalim_odenecek"),
    ]

    operations = [
        migrations.AlterField(
            model_name="malalim",
            name="odenecek",
            field=models.FloatField(blank=True, verbose_name="Ödenecek Tutar"),
        ),
    ]