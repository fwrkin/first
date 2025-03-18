# Generated by Django 5.1.4 on 2025-01-21 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
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
                    "name",
                    models.CharField(
                        help_text="Введите заголовок поста",
                        max_length=255,
                        verbose_name="Заголовок",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Введите содержание поста",
                        null=True,
                        verbose_name="Содержание",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        help_text="Вставьте изображение для поста",
                        null=True,
                        upload_to="blog/image",
                        verbose_name="Превью",
                    ),
                ),
                (
                    "created_at",
                    models.DateField(
                        blank=True,
                        help_text="Введите дату создания",
                        null=True,
                        verbose_name="Дата создания",
                    ),
                ),
                (
                    "was_publication",
                    models.BooleanField(
                        default=True,
                        help_text="Опубликован пост?",
                        verbose_name="Опубликован пост",
                    ),
                ),
                (
                    "views_counter",
                    models.PositiveIntegerField(
                        default=0,
                        help_text="Введите количество просмотров",
                        verbose_name="Количество просмотров",
                    ),
                ),
            ],
            options={
                "verbose_name": "Пост",
                "verbose_name_plural": "Посты",
                "ordering": ["description", "name"],
            },
        ),
        migrations.DeleteModel(
            name="Paper",
        ),
    ]
