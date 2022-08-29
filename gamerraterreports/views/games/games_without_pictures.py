"""Module for generating Games without pictures report"""
from django.shortcuts import render
from django.db import connection
from django.views import View

from gamerraterreports.views.helpers import dict_fetch_all


class GamesWithoutPictures(View):
    def get(self, request):
        with connection.cursor() as db_cursor:

            # TODO: Write a query to get  top five games by rating
            db_cursor.execute("""
            SELECT
                p.game_id,
                g.id AS game,
                g.title
            FROM gamerapi_game g 
            LEFT JOIN gamerapi_picture p ON g.id = p.game_id
            WHERE p.game_id is null
            """)
            # Pass the db_cursor to the dict_fetch_all function to turn the fetch_all() response into a dictionary
            dataset = dict_fetch_all(db_cursor)

            games_without_pictures = []

            for row in dataset:
                # TODO: Create a dictionary called game 
                game = {
                    "game": row['game'],
                    "title": row['title']
                }

                games_without_pictures.append(game)
        
        # The template string must match the file name of the html template
        template = 'games/games_without_pictures.html'
        
        # The context will be a dictionary that the template can access to show data
        context = {
            "game_list": games_without_pictures
        }

        return render(request, template, context)