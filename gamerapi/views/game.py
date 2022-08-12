from gamerapi.models import Game, Player, Category
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.http import HttpResponseServerError


class GameView(ViewSet):
    """Gamer Rater Games View

    Args:
        ViewSet(class): It is a class that combines related views. It is a type of class-based
        View, that does not provide any method handlers such as .get() or .post(),
         it instead provides actions such as .list() and .create()


         The game variable is now a list of GameObjects. 
         Just like in the retrieve, we’ll pass the game to the same 
         serializer class. This time adding many=True to let the serializer
        know that a list vs. a single object is to be serialized.
         """

    def list(self, request):
        """Handle Get requests to all the game types

        Returns:
            Response -- JSON serialized list of games
            """
        # New variable games, gets a list of all the game objects returned to it
        games = Game.objects.all()
        # Then the data from games is passed to the serializer and stored in serializer,
        # many=True is added so that is known it is a list
        serializer = GameSerializer(games, many=True)
        # Then the data is stored in serializer and is returned in JSON format
        return Response(serializer.data)

    def retrieve(self, request, pk):
        """ Handles the GET request for a single game. If one is not found
        it will return a 404

        Args: request (dict): the query parameter for the request
        pk (int): primary key of the game being requested.

        Returns:
            response: JSON serializer game for rhe selected key

            After getting the game, it is passed to the serializer. Lastly, 
            the serializer.data is passed to the Response as the response body. Using Response 
            combines what we were doing with the _set_headers and wfile.write functions.
        """
        try:
            # Matching the recieved primary key to the list of games primary keys
            game = Game.objects.get(pk=pk)
            serializer = GameSerializer(game)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Game.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        """Handles the POST operation

        Args:
            request (dict): The Object that is being created.

        Returns: 
            Response: JSON serialized game instance"""
        # Variable that stores gets and stores the logged in user
        player = Player.objects.get(user=request.auth.user)

        # Game variable declared, and the parameters of the fields,
        # are being passed to the create method.
        game = Game.objects.create(
            title=request.data["title"],
            description=request.data["description"],
            designer=request.data["designer"],
            year_released=request.data["year_released"],
            number_of_players=request.data["number_of_players"],
            estimated_time_to_play=request.data["estimated_time_to_play"],
            age_recommendation=request.data["age_recommendation"],
            player=player
        )
        game.categories.add(request.data["category"])
        serializer = GameSerializer(game)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GameSerializer(serializers.ModelSerializer):
    """JSON serializer for games
    Args:
        The serializer class determines how the Python data should be serialized to be sent back to the client.
        
        serializers (class): the serializer class which gives you a powerful, generic way to control the 
        output of your responses. ModelSerializer class which provides a useful shortcut
        for creating serializers that deal with model instances and querysets.
    """
    class Meta:
        """Meta is the inner class of the model class, it is used to change the behavior
        of your model fields
        
        The Meta class holds the configuration for the serializer. We’re telling the serializer to use the Game model and to include all of its fields."""
        model = Game
        fields = ('id', 'title', 'description', 'designer', 'year_released', 'number_of_players',
                  'estimated_time_to_play', 'age_recommendation', 'player', 'categories')
        depth = 1
