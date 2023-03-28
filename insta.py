from instapy import InstaPy
from instapy.util import smart_run

# Importing InstaPy should come before the emoji import
from emoji import UNICODE_EMOJI

# Rest of your code goes here

session = InstaPy(username='shoely.npl', password='S1h2o3e4l5y6##',)
session.login()
session.set_relationship_bounds(min_followers=10, max_followers=20)
session.follow_user_followers(['shoesmanduofficial'], amount=15, sleep_delay=7)
session.end()
