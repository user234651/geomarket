# orders/models.py
from django.db import models
from shop.models import Product  # ваша модель товара, убедитесь в корректном пути

class Order(models.Model):
    full_name = models.CharField("ФИО", max_length=100)
    email = models.EmailField("Email")
    card_number = models.CharField("Номер карты", max_length=20)
    bank = models.CharField("Банк", max_length=50)
    comment = models.TextField("Комментарий", blank=True, null=True)
    created_at = models.DateTimeField("Дата заказа", auto_now_add=True)

    def __str__(self):
        return f"Заказ #{self.id} от {self.full_name}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField("Количество", default=1)
    price = models.DecimalField("Цена за шт.", max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} (x{self.quantity})"
