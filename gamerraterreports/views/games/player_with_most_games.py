"""Module for generating bottom 5 games by rating report"""
from django.shortcuts import render
from django.db import connection
from django.views import View

from gamerraterreports.views.helpers import dict_fetch_all


class PlayerWithMostGames(View):
    def get(self, request):
        with connection.cursor() as db_cursor:

            # TODO: Write a query to get  top five games by rating
            db_cursor.execute("""
            SELECT name, MAX(number) AS total_games
            FROM (
            SELECT 
                u.first_name||' '||u.last_name AS name, 
                COUNT(g.player_id) AS number
            FROM auth_user u 
            JOIN gamerapi_player p ON u.id = p.user_id
            JOIN gamerapi_game g ON p.id = g.player_id
            GROUP BY name);
            """)
            # Pass the db_cursor to the dict_fetch_all function to turn the fetch_all() response into a dictionary
            dataset = dict_fetch_all(db_cursor)

            player_with_most_games = []

            for row in dataset:
                # TODO: Create a dictionary called game 
                game = {
                    "name": row['name'],
                    "total_games": row['total_games']
                }

                player_with_most_games.append(game)
        
        # The template string must match the file name of the html template
        template = 'games/player_with_most_games.html'
        
        # The context will be a dictionary that the template can access to show data
        context = {
            "game_list": player_with_most_games
        }

        return render(request, template, context)