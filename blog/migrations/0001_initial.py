# Generated by Django 5.1.4 on 2025-01-10 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Paper",
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
                (
                    "title",
                    models.CharField(max_length=300, verbose_name="Название статьи"),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, null=True, verbose_name="Описание статьи"
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True, upload_to="", verbose_name="Превью статьи"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создания"
                    ),
                ),
                (
                    "publication",
                    models.BooleanField(
                        default=True, verbose_name="Признак публикации"
                    ),
                ),
                (
                    "views",
                    models.IntegerField(
                        default=0, verbose_name="Количество просмотров"
                    ),
                ),
            ],
            options={
                "verbose_name": "Статья",
                "verbose_name_plural": "Статьи",
                "ordering": ["title", "description"],
            },
        ),
    ]
