# core/models.py

from django.db import models
from django.contrib.auth.models import User   # Django's built-in User model


class Item(models.Model):
    """
    Represents a single lost or found item report.
    Each item is linked to the user who reported it.
    """

    # Choices for item type
    ITEM_TYPE_CHOICES = [
        ('lost',  'Lost'),
        ('found', 'Found'),
    ]

    # Who reported this item (linked to Django's built-in User)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Is this a "lost" report or a "found" report?
    item_type = models.CharField(max_length=10, choices=ITEM_TYPE_CHOICES)

    # Item details filled in by the user
    item_name    = models.CharField(max_length=100)
    description  = models.TextField()
    location     = models.CharField(max_length=200)
    date_time    = models.DateTimeField()
    contact_info = models.CharField(max_length=100, blank=True)  # optional

    # Optional photo upload — saved inside media/items/ folder
    image = models.ImageField(upload_to='items/', blank=True, null=True)

    # Automatically saves when this record was created
    reported_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # This shows a readable name in Django Admin
        return f"[{self.item_type.upper()}] {self.item_name} — {self.user.username}"