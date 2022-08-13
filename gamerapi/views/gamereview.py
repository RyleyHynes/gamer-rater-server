from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from gamerapi.models import Review, Game, Player
from django.contrib.auth.models import User


class GameReviewSerializer(serializers.ModelSerializer):
    """JSON serializer for game reviews
    """
    class Meta:
        model = Review
        fields = ('id', 'review', 'game', 'player')

# Create a user serializer, to only return certain fields from user model


class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for users, to have only the id, username, and name fields return
    """
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'user_name')

# Created the player serializer and used the user serializer to include users info into that
# was selected in the US above, so that fields not needed are not brought in.


class PlayerSerializer(serializers.ModelSerializer):
    """JSON serializer for player date received
    """
    class Meta:
        model = Player
        # Selected the fields to return in the player object, the user data returns as an
        # object in player
        fields = ('id', 'bio', 'user')


class GameReviewView(ViewSet):
    """GamerApi Review View"""

    def retrieve(self, request, pk):
        """Handle Get requests for single review

        Returns:
            Response -- JSON serialized review
        """
        try:
            review = Review.objects.get(pk=pk)
            serializer = GameReviewSerializer(review)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Review.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle Get requests for all reviews

        Returns:
            Response -- JSON serialized list of reviews
        """
        game_param = self.request.query_params.get('gameId', None)
        if game_param is not None:
            reviews = Review.objects.filter(game_id=game_param)
        else:
            reviews = Review.objects.all()
        serializer = GameReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized game instance
        """
        game = Game.objects.get(pk=request.data["game"])
        player = Player.objects.get(user=request.auth.user)

        review = Review.objects.create(
            review=request.data["review"],
            game=game,
            player=player
        )
        serializer = GameReviewSerializer(review)
        return Response(serializer.data)
