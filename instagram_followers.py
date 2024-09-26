from instagrapi import Client
# Credentials
username = ''
password = ''
# Create Client for your instagram account
client = Client()
client.login(username=username, password=password)
user_id = client.user_id_from_username(password)
# Get Followers
followers = client.user_followers(user_id)
# Get Followings
followings = client.user_following(user_id)
# Check and print any following username that isn't in the followers
for following in followings:
    if followings[following].username not in [followers[follower].username for follower in followers]:
        print(followings[following].username)