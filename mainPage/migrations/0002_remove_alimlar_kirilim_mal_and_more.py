# Generated by Django 4.1.3 on 2023-07-08 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mainPage", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="alimlar_kirilim", name="mal",),
        migrations.RemoveField(model_name="alimlar_kirilim", name="tedarikEden",),
        migrations.RemoveField(model_name="malgiris", name="mal1",),
        migrations.RemoveField(model_name="malgiris", name="mal1a",),
        migrations.RemoveField(model_name="malgiris", name="mal1b",),
        migrations.RemoveField(model_name="malgiris", name="mal1c",),
        migrations.RemoveField(model_name="malgiris", name="mal2",),
        migrations.RemoveField(model_name="malgiris", name="mal2a",),
        migrations.RemoveField(model_name="malgiris", name="mal2b",),
        migrations.RemoveField(model_name="malgiris", name="mal2c",),
        migrations.RemoveField(model_name="malgiris", name="mal3",),
        migrations.RemoveField(model_name="malgiris", name="mal3a",),
        migrations.RemoveField(model_name="malgiris", name="mal3b",),
        migrations.RemoveField(model_name="malgiris", name="mal3c",),
        migrations.RemoveField(model_name="malgiris", name="mal4",),
        migrations.RemoveField(model_name="malgiris", name="mal4a",),
        migrations.RemoveField(model_name="malgiris", name="mal4b",),
        migrations.RemoveField(model_name="malgiris", name="mal4c",),
        migrations.RemoveField(model_name="malgiris", name="mal5",),
        migrations.RemoveField(model_name="malgiris", name="mal5a",),
        migrations.RemoveField(model_name="malgiris", name="mal5b",),
        migrations.RemoveField(model_name="malgiris", name="mal5c",),
        migrations.RemoveField(model_name="malgiris", name="tedarikEden",),
        migrations.DeleteModel(name="Alimlar",),
        migrations.DeleteModel(name="Alimlar_Kirilim",),
        migrations.DeleteModel(name="MalGiris",),
    ]
