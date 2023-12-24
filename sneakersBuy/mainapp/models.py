from django.db import models


class Category(models.Model):
    name = models.CharField(
        verbose_name="Имя ",
        max_length=64,
        unique=True,
    )

    description = models.TextField(
        verbose_name="Описание ",
        blank=True,
    )

    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория",
        verbose_name_plural = "Категория"


class Brand(models.Model):
    name = models.CharField(
        verbose_name="Имя ",
        max_length=64,
        unique=True,
    )

    description = models.TextField(
        verbose_name="Описание ",
        blank=True,
    )

    image = models.ImageField(
        upload_to='brand_images',
        blank=True,
        verbose_name="Изображение"
    )

    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Бренд",
        verbose_name_plural = "Бренды"


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="категория"
    )

    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        verbose_name="бренд",
        default=None,
    )

    name = models.CharField(
        verbose_name="Имя продукта",
        max_length=128
    )

    image = models.ImageField(
        upload_to='product_images',
        blank=True,
        verbose_name="Изображение"
    )

    short_desc = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Краткое описание"
    )

    description = models.TextField(
        blank=True,
        verbose_name="Описание",
    )

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0,
        verbose_name="Цена "
    )

    quantity = models.PositiveIntegerField(
        default=0,
        verbose_name="Количество товара на складе",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт",
        verbose_name_plural = "Продукты"
