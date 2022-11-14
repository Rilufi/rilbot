import random, time, tweepy
from auth import api_xame, api_uva, api_mevu, api, api_zark, api_lufi, api_woba, api_maj, api_zeld, api_uff


# Randomly unfollows users if the authenticating user's following number is greater than 3000 until it's 2999


class unfollow:
    my_screen_name = api.me().screen_name

    def unfollow(self):

        if api.me().friends_count > 3000:
            print(f'Current following count is at {api.me().friends_count}.')
            for count, friend in enumerate(tweepy.Cursor(api.friends).items(api.me().friends_count)):
                
                if count <= 500:
                    print(f'{count}. User was recently followed.' )
                    continue
                
                # Checks if user is following authenticating user
                elif self.following_me(friend.screen_name):
                    print(f'{count}. {friend.screen_name} follows {self.my_screen_name}.')
                    continue
                
                # Randomly skips users
                elif random.randint(0, 1) == 1:
                    print(f'{count}. User has been skipped.')
                    continue
                
                # Ends loop if following count is 2999
                elif api.me().friends_count == 2999:
                    break
                
                else:
                    api.destroy_friendship(friend.screen_name)
                    print(f'{count}. {friend.screen_name} has been unfollowed.')
                    time.sleep(2.5)
        else:
            print(f'Following count is at {api.me().friends_count}. No unfollowing needed.')
    
    # Checks if a user is following the authenticating user
    def following_me(self, screen_name):
        status = api.show_friendship(source_screen_name = screen_name, target_screen_name = self.my_screen_name)
        return status[0].following
