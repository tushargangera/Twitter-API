import tweepy
import configparser
import pandas as pd
from translate import Translator


def getDataFromTwitter():
    config = configparser.ConfigParser()
    config.read('config.ini')
    api_key = config['twitter']['api_key']
    api_key_secret = config['twitter']['api_key_secret']
    access_token = config['twitter']['access_token']
    access_token_secret = config['twitter']['access_token_secret']
    
    try:
        auth = tweepy.OAuthHandler(api_key,api_key_secret)
        auth.set_access_token(access_token,access_token_secret)
        api = tweepy.API(auth)
        public_tweets = api.home_timeline()
        print(public_tweets)
        columns = ['tweet_timeline','user','tweet_text']
        data = []
        for  tweets in public_tweets:
            data.append([tweets.created_at,tweets.user.screen_name,tweets.text])
        df =pd.DataFrame(data,columns)
        print(df)

        keywords = '@QuickPay_SNB'
        limit = 10

        hashtag_tweets = tweepy.Cursor(api.search_tweets,q=keywords,count=100,tweet_mode='extended').items(limit)
        hashtag_data = []
        searchtags_columns = ['users','tweet']

        for tweet in hashtag_tweets:
            hashtag_data.append([tweet.user.screen_name,tweet.full_text])

        hashtags_df = pd.DataFrame(hashtag_data,searchtags_columns)
         
        print(hashtags_df)
         
    except:
        print("*************************")  
        print("Twitter connection failed")  
        print("*************************")    

def translate(str):
    print("Translate function called with ===> "+ str)
    text = "السلام عليكم. أنا على وشك التقاعد. بقيت 6 أشهر حتى التقاعد. هل يجوز لي أن أرهن؟"
    list_of_text = text.split(' ')
    try:
        translator= Translator(from_lang="arabic",to_lang="english")
        translation = translator.translate(text)
        print(translation)
    except:
        print("not able to translate")
        for texts in list_of_text:
            translation = translator.translate(texts)
            print(translation)

def stringFinder(text:str):
    Negitive_identifiers = ['sorry', '😡','not happy','bad']
    positive_identifiers = ['thanks','thank you','good']
    s = text
    n_count = 0
    p_count = 0
    for n in Negitive_identifiers:
        if n in s:
            n_count = n_count + 1

    for p in positive_identifiers:
        if p in s:
            p_count = p_count + 1        

    if n_count > 0:
        print("Negitive sentiment")
    else:
        if p_count > 0:
            print("positive sentiment")
        else:
            print("Neutral sentiment")


def main():
    stringFinder('Through the website, I opened an investment account, and I received a message from you, dear customer. The trading portfolio has been opened in the Saudi market No. ***, which is linked to your cash account No. ***. He called Al-Ahly Capital, saying, “Sorry, you do not have a trading portfolio.” 🙄😡')
    stringFinder('thank you for the support')

if __name__ == "__main__":
    main()