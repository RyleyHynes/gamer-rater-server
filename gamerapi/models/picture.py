from django.db import models

# Step 1: Name the model and inherit from the Django Model class
class Picture(models.Model):
    # Step 2: Add any fields on the ERD
    picture_url = models.URLField()
    # On pictures there is now a list of pictures that this player is on
    player = models.ForeignKey("Player", on_delete=models.CASCADE, related_name="pictures")
    # On pictures there is now a list of pictures that this game is on
    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name="pictures")