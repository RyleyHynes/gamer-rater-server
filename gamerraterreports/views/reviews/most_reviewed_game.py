"""Module for generating Game with most reviews report"""
from django.shortcuts import render
from django.db import connection
from django.views import View

from gamerraterreports.views.helpers import dict_fetch_all


class MostReviewedGame(View):
    def get(self, request):
        with connection.cursor() as db_cursor:

            # TODO: Write a query to get  top five games by rating
            db_cursor.execute("""
            SELECT title, MAX(number) Number_Of_Reviews
            FROM (
            SELECT
                g.id,
                g.title AS title,
                COUNT(r.game_id) AS number
            FROM gamerapi_game g 
            JOIN gamerapi_review r ON g.id = r.game_id
            GROUP BY title);
            """)
            # Pass the db_cursor to the dict_fetch_all function to turn the fetch_all() response into a dictionary
            dataset = dict_fetch_all(db_cursor)

            most_reviewed_game = []

            for row in dataset:
                # TODO: Create a dictionary called game 
                game = {
                    "title": row['title'],
                    "Number_Of_Reviews": row['Number_Of_Reviews']
                }

                most_reviewed_game.append(game)
        
        # The template string must match the file name of the html template
        template = 'games/most_reviewed_game.html'
        
        # The context will be a dictionary that the template can access to show data
        context = {
            "game_list": most_reviewed_game
        }

        return render(request, template, context)
