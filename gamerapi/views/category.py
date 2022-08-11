from django.http import HttpResponseServerError
from gamerapi.models import Category, category
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status



class CategoryView(ViewSet):
    """
        Gamer Rater Categories View
    Args:
        ViewSet(class): It is a class that combines related views. It is a type of class-based
        View, that does not provide any method handlers such as .get() or .post(),
         it instead provides actions such as .list() and .create()


         The game variable is now a list of GameObjects. 
         Just like in the retrieve, we’ll pass the game to the same 
         serializer class. This time adding many=True to let the serializer
        know that a list vs. a single object is to be serialized.
         """

    def retrieve(self, request, pk):
        """Handle Get request for single Category Type"""
        try:
            category = Category.objects.get(pk=pk)
            serializer = CategorySerializer(category)
            return Response(serializer.data)
        except Category.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle Get Requests to all the categories

        Returns:
            Response -- JSON serialized list of category types
            """
        # New variable categories, gets a list of all the category objects returned to it
        categories = Category.objects.all()
        # Then the data from categories is passed to the serializer and stored in the serializer,
        # Many=True is added so that is known it is a list
        serializer = CategorySerializer(categories, many=True)
        # Then the data is stored in serializer and is returned in JSON format
        return Response(serializer.data)


class CategorySerializer(serializers.ModelSerializer):
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
        model = Category
        fields = ('id', 'name')
        depth = 1
