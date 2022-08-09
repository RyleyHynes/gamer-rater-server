from django.db import models

# Step 1: Name the model and inherit Django Model class
class Rating(models.Model):
    # Step 2: Add any fields on ERD
    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name="ratings")
    player = models.ForeignKey("Player", on_delete=models.CASCADE, related_name="ratings")
    rating = models.IntegerField(default=0)