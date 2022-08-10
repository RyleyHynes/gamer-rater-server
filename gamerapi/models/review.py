from django.db import models

# Step 1: Name model and inherit Django Model class


class Review(models.Model):
    # Step 2: Add any field on ERD
    review = models.CharField(max_length=300)
    # On reviews there is now a list of reviews that this game is on
    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name="reviews")
    # On reviews there is now a list of reviews that this player is on
    player = models.ForeignKey("Player", on_delete=models.CASCADE, related_name="reviews")

