"""Module for generating bottom 5 games by rating report"""
from django.shortcuts import render
from django.db import connection
from django.views import View

from gamerraterreports.views.helpers import dict_fetch_all


class GamesWithMoreThan5PlayersList(View):
    def get(self, request):
        with connection.cursor() as db_cursor:

            # TODO: Write a query to get  top five games by rating
            db_cursor.execute("""
            SELECT
                g.id,
                g.title,
                g.number_of_players
            FROM gamerapi_game g 
            WHERE number_of_players > 5;
            """)
            # Pass the db_cursor to the dict_fetch_all function to turn the fetch_all() response into a dictionary
            dataset = dict_fetch_all(db_cursor)

            games_with_more_than_5_players = []

            for row in dataset:
                # TODO: Create a dictionary called game 
                game = {
                    "id": row['id'],
                    "title": row['title'],
                    "number_of_players": row['number_of_players']
                }

                games_with_more_than_5_players.append(game)
        
        # The template string must match the file name of the html template
        template = 'games/more_than_5_players.html'
        
        # The context will be a dictionary that the template can access to show data
        context = {
            "game_list": games_with_more_than_5_players
        }

        return render(request, template, context)
