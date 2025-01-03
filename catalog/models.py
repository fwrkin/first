from django.db import models


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
        upload_to='product/photo',
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

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "description", "category", "price"]

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
