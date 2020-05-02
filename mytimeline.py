import tweepy
import datetime
import os
import pprint
import time
import urllib.error
import urllib.request
import MeCab
import re

# 自分がフォローしている人がいいねまたはリツイートした画像のうち自分がいいと思ったやつを取得
# 自分がフォローしている人を見つける

def getApiInstance():

    Consumer_key = 'PpC1XL0KswKbq1lHUE6g4kkPA'
    Consumer_secret = 'HuTx1G1uxKiGyzu6AvzF2PQpcSrAxvlDGy7dSKsFeWHJ84yezT'
    Access_token = '1000380378312404994-3xf6YHeoR8swL7PIVOUm80UtQih06W'
    Access_secret = 'hT22RZjMpEeBDlmiAHmqEzGng8hk8VcBptRhcWWZpHD5b'

    #認証
    auth = tweepy.OAuthHandler(Consumer_key, Consumer_secret)
    auth.set_access_token(Access_token, Access_secret)

    api = tweepy.API(auth, wait_on_rate_limit = True)

    return api

# def gettwitterdata(keyword,api):
#     #検索キーワード設定
#     q = keyword
#     i = 0
#     meishi = []
#     doushi = []
#
#     #つぶやきを格納するリスト
#     tweets_data =[]
#
#     #カーソルを使用してデータ取得
#     for tweet in tweepy.Cursor(api.search, q=q, count=100,tweet_mode='extended').items():
#         if tweet.created_at < datetime.datetime.now() + datetime.timedelta(hours=8):
#             pass

def printTweetBySearch(s):
  api = getApiInstance() # 認証

  # tweets = tweepy.Cursor(api.search, q = s,       # APIの種類と検索文字列
  #                        include_entities = True, # 省略されたリンクを全て取得
  #                        tweet_mode = 'extended', # 省略されたツイートを全て取得
  #                        lang = 'ja').items()       # 日本のツイートのみ取得

  tweets = tweepy.Cursor(api.user_timeline,
                         tweet_mode = 'extended',
                         include_entities = True, # 省略されたリンクを全て取得
                         lang = 'ja').items()       # 日本のツイートのみ取得

  for tweet in tweets:
      print(tweet)
      print('＝＝＝＝＝＝＝＝＝＝')
      print('twid : ',tweet.id)               # tweetのIDを出力。ユニークなもの
      print('user : ',tweet.user.screen_name) # ユーザー名
      print('date : ', tweet.created_at)      # 呟いた日時
      print(tweet.full_text)                  # ツイート内容
      print('favo : ', tweet.favorite_count)  # ツイートのいいね数
      print('retw : ', tweet.retweet_count)   # ツイートのリツイート数
      print('date : ', tweet.expanded_entities)
      break


def main():
  printTweetBySearch('しもやけ')

if __name__ == "__main__":
  main()
