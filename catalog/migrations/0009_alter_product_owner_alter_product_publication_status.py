# Generated by Django 4.2.2 on 2025-03-26 22:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("catalog", "0008_alter_product_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                help_text="Укажите владельца продукта",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Владелец продукта",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="publication_status",
            field=models.BooleanField(
                blank=True,
                default=True,
                help_text="Укажите, опубликован ли продукт",
                null=True,
                verbose_name="Статус публикации",
            ),
        ),
    ]
