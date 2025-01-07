# Generated by Django 5.1.4 on 2025-01-02 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="description",
            field=models.TextField(
                blank=True,
                help_text="Введите описание продукта",
                null=True,
                verbose_name="Описание продукта",
            ),
        ),
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(
                help_text="Введите название категории",
                max_length=150,
                verbose_name="Название продукта",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                help_text="Введите дату создания",
                verbose_name="Дата создания",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.TextField(
                blank=True,
                help_text="Введите описание продукта",
                null=True,
                verbose_name="Описание продукта",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(
                blank=True,
                help_text="Загрузите изображение продукта",
                null=True,
                upload_to="product/photo",
                verbose_name="Изображение продукта",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="updated_at",
            field=models.DateTimeField(
                auto_now=True,
                help_text="Введите дату последнего изменения",
                verbose_name="Дата последнего изменения",
            ),
        ),
    ]
