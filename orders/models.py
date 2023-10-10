from django.db import models

from customers.models import Customer


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    robot_serial = models.CharField(max_length=5, blank=False, null=False)


class WaitingList(Order):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE,
        related_name='waiting_list')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
