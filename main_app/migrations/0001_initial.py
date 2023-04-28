# Generated by Django 4.2 on 2023-04-24 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=100)),
                ("breed", models.CharField(max_length=100)),
                ("description", models.TextField(max_length=250)),
                ("age", models.IntegerField()),
            ],
        ),
    ]
