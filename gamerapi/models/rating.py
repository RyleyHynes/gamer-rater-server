from django.db import models

# Step 1: Name the model and inherit Django Model class
class Rating(models.Model):
    # Step 2: Add any fields on ERD
    rating = models.IntegerField(default=0)
    # On ratings there is now a list of ratings that this game is on
    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name="ratings")
    # On ratings there is now a list of ratings that this player is on
    player = models.ForeignKey("Player", on_delete=models.CASCADE, related_name="ratings")