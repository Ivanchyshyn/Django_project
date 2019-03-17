from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=100)
    summary = models.TextField()

    def get_absolute_url(self):
        return f'/detail/{self.id}/'
