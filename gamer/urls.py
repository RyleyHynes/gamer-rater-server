from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from gamerapi.views import register_user, login_user
from gamerapi.views.category import CategoryView
from gamerapi.views.game import GameView
from gamerapi.views.gamereview import GameReviewView
from gamerapi.views.picture import PictureView
from gamerapi.views.rating import RatingView


router = routers.DefaultRouter(trailing_slash=False)
# Left string is for error handling, right string is for the route (I am naming these, what really matters is the View)
router.register(r'games', GameView, 'game')
router.register(r'categories', CategoryView, 'category')
router.register(r'reviews', GameReviewView, 'review')
router.register(r'ratings', RatingView, 'ratings')
router.register(r'pictures', PictureView, 'picture')


urlpatterns = [
    # Requests to http://localhost:8000/register will be routed to the register_user function
    path('register', register_user),
    # Requests to http://localhost:8000/login will be routed to the login_user function
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('', include('gamerraterreports.urls')),
]