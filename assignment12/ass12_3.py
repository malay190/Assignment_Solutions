#Q.3- Using Tweepy library try to extract tweets from Twitter.

import tweepy

consumer_key_038="x4gCP3GKdAZteLrhmP5okLjfA"
consumer_secret_038="XoXNqNOrI51YVdCwtUFIGUAVWLOJ83OvmCI7zBj3fH5rBiC52E"

access_token_038="2919790812-7ojnQkrdt5DKcW7cMxumlo2WU4KbX8JYZqnTHT9"
access_token_secret_038="hDVkdg6F0DEgMGYsAEEezec09HShx9MpI2JQK69jmcIQu"

auth=tweepy.OAuthHandler(consumer_key_038,consumer_secret_038)
auth.set_access_token(access_token_038,access_token_secret_038)
api=tweepy.API(auth)

hastag="#"+input("entet the hastag you want to find:")
num=int(input("enter the number of text you want tp fetch:"))

tweets=api.search(hastag,lang="en",count=num,tweet_mode="extended")

for tweet in tweets:
	print(".....................")
	print(tweet.full_text)
	print(".....................")

