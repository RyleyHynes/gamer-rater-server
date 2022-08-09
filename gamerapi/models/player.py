from django.db import models
from django.contrib.auth.models import User

# Step 1: Name the model and inherit the Django Model class


class Player(models.Model):
    """The player model, inherits properties from the parent class module."""
    # Step 2: Add any fields on the ERD
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="user")
    bio = models.CharField(max_length=300)
