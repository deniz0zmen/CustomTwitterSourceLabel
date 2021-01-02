import tweepy
import time

auth = tweepy.OAuthHandler("CONSUMER KEY HERE","CONSUMER PRIVATE KEY HERE")
auth.set_access_token("ACCESS TOKEN HERE","PRIVATE ACCESS TOKEN HERE")
api = tweepy.API(auth)

print("Enter tweet:")
tweetMessage  = str(input())
print("Are you sure you want to tweet this:", tweetMessage)
confirm = str(input())

if confirm == "yes":
    try:
        api.update_status(tweetMessage)
        print("Tweet posted successfuly")
        input()
    except:
        print("Tweet failed. Please check your tokens (bearer token is not the same as the access token) or your Twitter developer account status.")
        time.sleep(1)
        print("if its still not working figure it out yourself i've made this script idiot proof enough")
        input()
else:
    print("ok")
    print("press enter to close")
    input()

