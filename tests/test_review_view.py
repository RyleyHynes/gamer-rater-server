from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from gamerapi.models import Review, Player
from gamerapi.views.gamereview import GameReviewSerializer

class ReviewTests(APITestCase):

    # Add any fixtures you want to run to build the test database
    fixtures = ['users', 'tokens', 'players', 'categories', 'games', 'reviews']
    def setUp(self):
        # Grab the first Player object from the database and add their token to the headers
        self.player = Player.objects.first()
        token = Token.objects.get(user=self.player.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")

    def test_create_review(self):
        """Create review test"""
        url = "/reviews"

        # Define the Review properties
        # The keys should match what the create method is expecting
        # Make sure this matches the code you have
        review = {
            "review": "Hey man this game is great!",
            "game": 1
        }

        response = self.client.post(url, review, format='json')

        # The _expected_ output should come first when using an assertion with 2 arguments
        # The _actual_ output will be the second argument
        # We _expect_ the status to be status.HTTP_201_CREATED and it _actually_ was response.status_code
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        
        # Get the last review added to the database, it should be the one just created
        new_review = Review.objects.last()

        # Since the create method should return the serialized version of the newly created game,
        # Use the serializer you're using in the create method to serialize the "new_game"
        # Depending on your code this might be different
        expected = GameReviewSerializer(new_review)

        # Now we can test that the expected ouput matches what was actually returned
        self.assertEqual(expected.data, response.data)


    def test_change_review(self):
        """Test update review"""
        review = Review.objects.first()

        url = f'/reviews/{review.id}'

        updated_review = {
            "review": f'{review.review}'
        }

        response = self.client.put(url, updated_review, format='json')

        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)

        # Refresh the review object to reflect any changes in the database
        review.refresh_from_db()

        # assert that the updated value matches
        self.assertEqual(updated_review['review'], review.review)