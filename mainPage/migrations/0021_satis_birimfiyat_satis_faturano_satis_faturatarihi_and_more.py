# Generated by Django 4.1.3 on 2023-08-26 20:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainPage", "0020_alter_kantar_faturatarihi"),
    ]

    operations = [
        migrations.AddField(
            model_name="satis",
            name="birimFiyat",
            field=models.FloatField(default=1, verbose_name="Birim Fiyat"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="satis",
            name="faturaNo",
            field=models.TextField(default=1, verbose_name="Fatura No"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="satis",
            name="faturaTarihi",
            field=models.DateField(
                default=datetime.datetime.today, verbose_name="Fatura Tarihi"
            ),
        ),
        migrations.AddField(
            model_name="satis",
            name="satisTarihi",
            field=models.DateTimeField(
                blank=True,
                default=datetime.datetime.now,
                null=True,
                verbose_name="Satış Tarihi",
            ),
        ),
    ]