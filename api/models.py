from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders", blank=True, null=True)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return f"{self.user}"


class Favourite(models.Model):
    quantity = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Избранное"
        verbose_name_plural = "Избранные"

    def __str__(self):
        return f"{self.products.all()}"

    def save(self, *args, **kwargs):
        print(self.products.all())
        self.quantity = self.products.all().count()
        return super().save(*args, **kwargs)


class Product(models.Model):
    name = models.CharField("Название", max_length=255)
    price = models.DecimalField("Цена", decimal_places=2, max_digits=10)
    storehouse = models.PositiveIntegerField("На складе")
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="products", verbose_name="Продавец", blank=True, null=True)
    phone_number = models.CharField("Телефон", max_length=13)
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING, related_name="products", blank=True, null=True)
    favourite = models.ForeignKey(Favourite, on_delete=models.DO_NOTHING, related_name="products", blank=True, null=True)
    
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return f"{self.name}"


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    photo = models.FileField(upload_to="images", blank=True, null=True)

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"

    def __str__(self):
        return f"{self.product}"