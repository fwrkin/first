from django.db import models

from users.models import User


class Product(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="Название продукта",
        help_text="Введите название продукта",
    )
    description = models.TextField(
        verbose_name="Описание продукта",
        help_text='Введите описание продукта',
        null=True,
        blank=True,
    )
    image = models.ImageField(
        upload_to='products/photo',
        verbose_name="Изображение продукта",
        help_text='Загрузите изображение продукта',
        blank=True,
        null=True,
    )
    category = models.CharField(
        max_length=150,
        verbose_name="Категория продукта",
        help_text="Введите категорию продукта",
    )
    price = models.FloatField(
        verbose_name="Стоимость продукта",
        help_text="Введите стоимость продукта",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
        help_text='Введите дату создания',
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата последнего изменения',
        help_text='Введите дату последнего изменения',
    )
    publication_status = models.BooleanField(
        default=True,
        blank=True,
        null=True,
        verbose_name="Статус публикации",
        help_text="Укажите, опубликован ли продукт"
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Владелец продукта",
        help_text="Укажите владельца продукта",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "description", "category", "price"]
        permissions = [
            ("can_edit_product", "Can edit product"),
            ('can_unpublish_product', 'Can unpublish product'),
            ('can_delete_product', 'Can delete product'),
        ]

    def __str__(self):
        return f"{self.name} {self.description}"


class Category(models.Model):
    objects = None
    name = models.CharField(
        max_length=150,
        verbose_name="Название продукта",
        help_text='Введите название категории'
    )
    description = models.TextField(
        verbose_name="Описание продукта",
        help_text='Введите описание продукта',
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name", "description"]

    def __str__(self):
        return f"{self.name} {self.description}"
