# Generated by Django 4.2.2 on 2023-08-10 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainPage", "0012_malalim_odenecek_alter_malalim_hurda"),
    ]

    operations = [
        migrations.AlterField(
            model_name="malalim",
            name="odenecek",
            field=models.FloatField(default=0, verbose_name="Ödenecek Tutar"),
            preserve_default=False,
        ),
    ]
