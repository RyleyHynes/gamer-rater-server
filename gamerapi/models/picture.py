from django.db import models

# Step 1: Name the model and inherit from the Django Model class
class Picture(models.Model):
    # Step 2: Add any fields on the ERD
    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name="pictures")
    player = models.ForeignKey("Player", on_delete=models.CASCADE, related_name="pictures")
    picture_url = models.URLField()