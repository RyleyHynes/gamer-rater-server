"""Module for generating bottom 5 games by rating report"""
from django.shortcuts import render
from django.db import connection
from django.views import View

from gamerraterreports.views.helpers import dict_fetch_all


class BottomFiveGameList(View):
    def get(self, request):
        with connection.cursor() as db_cursor:

            # TODO: Write a query to get  top five games by rating
            db_cursor.execute("""
            SELECT
                g.id,
                g.title,
                r.rating
            FROM gamerapi_game g 
            JOIN gamerapi_rating r ON g.id = r.game_id
            ORDER BY rating ASC
            LIMIT 5;
            """)
            # Pass the db_cursor to the dict_fetch_all function to turn the fetch_all() response into a dictionary
            dataset = dict_fetch_all(db_cursor)

            top_5_games_by_rating = []

            for row in dataset:
                # TODO: Create a dictionary called game 
                game = {
                    "id": row['id'],
                    "title": row['title'],
                    "rating": row['rating']
                }

                top_5_games_by_rating.append(game)
        
        # The template string must match the file name of the html template
        template = 'ratings/top_5_games_by_rating.html'
        
        # The context will be a dictionary that the template can access to show data
        context = {
            "game_list": top_5_games_by_rating
        }

        return render(request, template, context)
