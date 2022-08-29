from django.urls import path
from gamerraterreports.views.games.games_for_kids_under_8 import GamesForKidsUnder8
from gamerraterreports.views.games.games_without_pictures import GamesWithoutPictures

from gamerraterreports.views.games.more_than_5_players import GamesWithMoreThan5PlayersList
from gamerraterreports.views.games.player_with_most_games import PlayerWithMostGames
from gamerraterreports.views.reviews.most_reviewed_game import MostReviewedGame

from .views import GamesByCategoryList
from .views import TopFiveGameList
from .views import BottomFiveGameList
from .views import GamesWithMoreThan5PlayersList
from .views import MostReviewedGame
from .views import GamesForKidsUnder8
from .views import GamesWithoutPictures

urlpatterns = [
    path('reports/top_5_games', TopFiveGameList.as_view()),
    path('reports/bottom_5_games', BottomFiveGameList.as_view()),
    path('reports/games_by_category', GamesByCategoryList.as_view()),
    path('reports/more_than_5_players', GamesWithMoreThan5PlayersList.as_view()),
    path('reports/most_reviewed_game', MostReviewedGame.as_view()),
    path('reports/player_with_most_games', PlayerWithMostGames.as_view()),
    path('reports/games_for_kids_under_8', GamesForKidsUnder8.as_view()),
    path('reports/games_without_pictures', GamesWithoutPictures.as_view()),


]