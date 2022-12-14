from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status

from gamerapi.models import Rating, Player, Game


class RatingView(ViewSet):
    """ Gamer Rater Rating View
    """

    def list(self, request):
        """Handles the get request for the rating
        Returns:
            Response: JSON serialized list of rating
        """
        game_param = self.request.query_params.get('gameId', None)
        if game_param is not None:
            ratings = Rating.objects.filter(game_id=game_param)

        else:
            ratings = Rating.objects.all()

        serializer = RatingSerializer(ratings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        """Handles the POST operation
        Returns:
            Response: JSON serialized game instance
        """
        # getting the logged in user id
        player = Player.objects.get(user=request.auth.user)
        # getting the game pk
        game = Game.objects.get(pk=request.data["game"])

        rating = Rating.objects.create(
            rating=request.data["rating"],
            player=player,
            game=game
        )

        serializer = RatingSerializer(rating)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handles PUT requests for the rating, only the maker can edit

        Returns:
            Response: Empty body with a 204 status code.
            """

        # getting the game by its primary key
        rating = Rating.objects.get(pk=pk)
        # Setting the fields to the values coming in
        rating.rating = request.data["rating"]
        # Saving selections
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class RatingSerializer(serializers.ModelSerializer):
    """JSON serializer for rating
    """

    class Meta:
        model = Rating
        fields = ('id', 'rating', 'game', 'player')