"""Module for generating bottom 5 games by rating report"""
from django.shortcuts import render
from django.db import connection
from django.views import View

from gamerraterreports.views.helpers import dict_fetch_all


class GamesByCategoryList(View):
    def get(self, request):
        with connection.cursor() as db_cursor:

            # TODO: Write a query to get  top five games by rating
            db_cursor.execute("""
            SELECT 
                c.id,
                c.name name,
                COUNT(gc.game_id) category_total
            FROM gamerapi_game g 
            JOIN gamerapi_gamecategories gc ON g.id = gc.game_id
            JOIN gamerapi_category c ON c.id = gc.category_id
            GROUP BY name;
            """)
            # Pass the db_cursor to the dict_fetch_all function to turn the fetch_all() response into a dictionary
            dataset = dict_fetch_all(db_cursor)

            games_by_category = []

            for row in dataset:
                # TODO: Create a dictionary called game 
                game = {
                    "id": row['id'],
                    "name": row['name'],
                    "category_total": row['category_total']
                }

                games_by_category.append(game)
        
        # The template string must match the file name of the html template
        template = 'games/games_by_category.html'
        
        # The context will be a dictionary that the template can access to show data
        context = {
            "game_list": games_by_category
        }

        return render(request, template, context)
