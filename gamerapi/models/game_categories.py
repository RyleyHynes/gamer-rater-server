from django.db import models


# Step 1: Name the model and inherit the django Model class
class GameCategories(models.Model):
    # Step 2: Add any fields on the erd
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
