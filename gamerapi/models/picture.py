from django.db import models

# Step 1: Name the model and inherit from the Django Model class


class Picture(models.Model):
    # Step 2: Add any fields on the ERD
    # On pictures there is now a list of pictures that this game is on
    game = models.ForeignKey(
        "Game", on_delete=models.DO_NOTHING, related_name="pictures")
    action_pic = models.ImageField(
        upload_to='actionimages', height_field=None, width_field=None, max_length=None, null=True)
