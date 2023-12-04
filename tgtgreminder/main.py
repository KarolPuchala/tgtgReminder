from tgtg import TgtgClient

from config import ACCESS_TOKEN, REFRESH_TOKEN, USER_ID, COOKIE

client = TgtgClient(access_token=ACCESS_TOKEN, 
                    refresh_token=REFRESH_TOKEN, 
                    user_id=USER_ID, 
                    cookie=COOKIE)

favorites = client.get_favorites()

for item in favorites:
    print(item['display_name'], item['items_available'])
