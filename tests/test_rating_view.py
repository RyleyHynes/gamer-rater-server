from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from gamerapi.models import Rating, Player
from gamerapi.views.rating import RatingSerializer

class RatingTests(APITestCase):

    # Add any fixtures you want to run to build the test database
    fixtures = ['users', 'tokens', 'players', 'categories', 'games', 'ratings']
    def setUp(self):
        # Grab the first Player object from the database and add their token to the headers
        self.player = Player.objects.first()
        token = Token.objects.get(user=self.player.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")

    def test_create_rating(self):
        """Create rating test"""
        url = "/ratings"

        # Define the Rating properties
        # The keys should match what the create method is expecting
        # Make sure this matches the code you have
        rating = {
            "rating": 5,
            "game": 1
        }

        response = self.client.post(url, rating, format='json')

        # The _expected_ output should come first when using an assertion with 2 arguments
        # The _actual_ output will be the second argument
        # We _expect_ the status to be status.HTTP_201_CREATED and it _actually_ was response.status_code
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        
        # Get the last rating added to the database, it should be the one just created
        new_rating = Rating.objects.last()

        # Since the create method should return the serialized version of the newly created game,
        # Use the serializer you're using in the create method to serialize the "new_game"
        # Depending on your code this might be different
        expected = RatingSerializer(new_rating)

        # Now we can test that the expected ouput matches what was actually returned
        self.assertEqual(expected.data, response.data)


    def test_change_rating(self):
        """Test update rating"""
        rating = Rating.objects.first()

        url = f'/ratings/{rating.id}'

        updated_rating = {
            "rating": 5
        }

        response = self.client.put(url, updated_rating, format='json')

        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)

        # Refresh the game object to reflect any changes in the database
        rating.refresh_from_db()

        # assert that the updated value matches
        self.assertEqual(updated_rating['rating'], rating.rating)