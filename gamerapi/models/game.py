from django.db import models

from gamerapi.models.game_category import Game_Category
# Step 1: Name the model and inherit from the django Model class


class Game(models.Model):
    # Step 2: Add any fields on the erd
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    designer = models.CharField(max_length=50)
    year_released = models.PositiveIntegerField(default=0)
    number_of_players = models.PositiveIntegerField(default=0)
    estimated_time_to_play = models.PositiveIntegerField(default=0)
    age_recommendation = models.SmallIntegerField(default=0)
    # On games there is now a list of games that this players on
    player = models.ForeignKey("Player", on_delete=models.CASCADE, related_name="games")
    # On games there is now a list of games that this category is on
    category = models.ManyToManyField("Category", through=Game_Category, related_name="games")