from django.db import models

# Step 1: Name model and inherit Django Model class


class Review(models.Model):
    # Step 2: Add any field on ERD
    game = models.ForeignKey(
        "Game", on_delete=models.CASCADE, related_name="reviews")
    player = models.ForeignKey(
        "Player", on_delete=models.CASCADE, related_name="reviews")
    review = models.CharField(max_length=300)
