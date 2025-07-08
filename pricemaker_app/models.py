from django.db import models

class PriceEntry(models.Model):
    ISIN_SOURCES = [
        ('BBG', 'Bloomberg'),
        ('TK', 'Thomson Reuters'),
        ('Reuters', 'Reuters'),
        ('Autre', 'Autre')
    ]
    isin = models.CharField(max_length=12)
    quotation_date = models.DateField()
    price = models.DecimalField(max_digits=12, decimal_places=4)
    currency = models.CharField(max_length=3, default='EUR')
    source = models.CharField(max_length=10, choices=ISIN_SOURCES)
    entered_by = models.CharField(max_length=100)
    entered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.isin} - {self.quotation_date} - {self.price}"
