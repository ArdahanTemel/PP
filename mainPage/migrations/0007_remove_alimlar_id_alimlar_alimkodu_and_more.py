# Generated by Django 4.2.2 on 2023-06-17 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainPage", "0006_alimlar_birimfiyat"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="alimlar",
            name="id",
        ),
        migrations.AddField(
            model_name="alimlar",
            name="alimKodu",
            field=models.IntegerField(
                default=1, primary_key=True, serialize=False, verbose_name="ID"
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="alimlar",
            name="birimFiyat",
            field=models.FloatField(verbose_name="Birim Fiyat"),
        ),
        migrations.AlterField(
            model_name="alimlar",
            name="miktar",
            field=models.FloatField(verbose_name="Ağırlık (kg)"),
        ),
    ]
