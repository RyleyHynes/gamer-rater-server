"""Module for generating bottom 5 games by rating report"""
from django.shortcuts import render
from django.db import connection
from django.views import View

from gamerraterreports.views.helpers import dict_fetch_all


class GamesForKidsUnder8(View):
    def get(self, request):
        with connection.cursor() as db_cursor:

            # TODO: Write a query to get  top five games by rating
            db_cursor.execute("""
            SELECT 
                g.id,
                g.title
            FROM gamerapi_game g
            WHERE g.age_recommendation < 8;
            """)
            # Pass the db_cursor to the dict_fetch_all function to turn the fetch_all() response into a dictionary
            dataset = dict_fetch_all(db_cursor)

            games_for_kids_under_8 = []

            for row in dataset:
                # TODO: Create a dictionary called game 
                game = {
                    "id": row['id'],
                    "title": row['title']
                }

                games_for_kids_under_8.append(game)
        
        # The template string must match the file name of the html template
        template = 'games/games_for_kids_under_8.html'
        
        # The context will be a dictionary that the template can access to show data
        context = {
            "game_list": games_for_kids_under_8
        }

        return render(request, template, context)
