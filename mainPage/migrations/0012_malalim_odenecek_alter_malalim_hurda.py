# Generated by Django 4.2.2 on 2023-08-10 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainPage", "0011_satis"),
    ]

    operations = [
        migrations.AddField(
            model_name="malalim",
            name="odenecek",
            field=models.FloatField(
                blank=True, null=True, verbose_name="Ödenecek Tutar"
            ),
        ),
        migrations.AlterField(
            model_name="malalim",
            name="hurda",
            field=models.FloatField(verbose_name="Fire"),
        ),
    ]