# Generated by Django 4.1.5 on 2023-01-16 00:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Social", "0002_cliente_emprendimiento"),
    ]

    operations = [
        migrations.CreateModel(
            name="comentario",
            fields=[
                (
                    "codigo",
                    models.PositiveBigIntegerField(primary_key=True, serialize=False),
                ),
                ("cuerpo", models.CharField(max_length=999)),
            ],
        ),
        migrations.AddField(
            model_name="cliente",
            name="emprendimientos",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="Social.emprendimiento",
            ),
        ),
        migrations.AddField(
            model_name="emprendimiento",
            name="comentarios",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="Social.comentario",
            ),
        ),
    ]