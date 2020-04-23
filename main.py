import tweepy
import datetime
import os
import pprint
import time
import urllib.error
import urllib.request

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


def Myfollowing(keyword,api):
    #検索キーワード設定
    q = keyword

    #つぶやきを格納するリスト
    tweets_data =[]

    followers_list = getFollowers_ids(api,"KparadiseT")#フォロワーの情報を取得
    for follower in followers_list:
        # friends_count : フォロー数
        # followers_count : フォロワー数
        # description : 概要（自己紹介が書かれているやつ）
        # print(follower.screen_name)
        # print(follower)
        get_image_tweet(follower,api)


def Myfriends(keyword,api):

    friends_list = getFriends_ids(api,"KparadiseT")#フォロワーの情報を取得
    for friend in friends_list:
        get_image_tweet(friend,api)


def get_image_tweet(user_id,api):

    list = api.user_timeline(user_id)
    for item in list:
        print(item.user.name)

        if 'media' in item.entities:
            url = item.entities['media'][0]['media_url_https']
            dst_path = url.split('/')[-1]
            download_file(url, './file/'+dst_path)


def getFollowers_ids(Api, Id):

    #Cursorを使ってフォロワーのidを逐次的に取得
    followers_ids = tweepy.Cursor(Api.followers_ids, id = Id, cursor = -1).items()

    followers_ids_list = []
    try:
        for followers_id in followers_ids:
            followers_ids_list.append(followers_id)
    except tweepy.error.TweepError as e:
        print(e.reason)

    return followers_ids_list


def getFriends_ids(Api, Id):

    #Cursorを使ってフォロワーのidを逐次的に取得
    friends_ids = tweepy.Cursor(Api.friends_ids, id = Id, cursor = -1).items()

    friends_ids_list = []
    try:
        for friends_id in friends_ids:
            friends_ids_list.append(friends_id)
    except tweepy.error.TweepError as e:
        print(e.reason)

    return friends_ids_list


def download_file(url, dst_path):
    try:
        with urllib.request.urlopen(url) as web_file:
            data = web_file.read()
            with open(dst_path, mode='wb') as local_file:
                local_file.write(data)
    except urllib.error.URLError as e:
        print(e)

def gettwitterdata(keyword):

    #python で Twitter APIを使用するためのConsumerキー、アクセストークン設定
    Consumer_key = 'PpC1XL0KswKbq1lHUE6g4kkPA'
    Consumer_secret = 'HuTx1G1uxKiGyzu6AvzF2PQpcSrAxvlDGy7dSKsFeWHJ84yezT'
    Access_token = '1000380378312404994-3xf6YHeoR8swL7PIVOUm80UtQih06W'
    Access_secret = 'hT22RZjMpEeBDlmiAHmqEzGng8hk8VcBptRhcWWZpHD5b'

    #認証
    auth = tweepy.OAuthHandler(Consumer_key, Consumer_secret)
    auth.set_access_token(Access_token, Access_secret)

    api = tweepy.API(auth, wait_on_rate_limit = True)

    #検索キーワード設定
    q = keyword

    #つぶやきを格納するリスト
    tweets_data =[]

    #カーソルを使用してデータ取得
    for tweet in tweepy.Cursor(api.search, q=q, count=100,tweet_mode='extended').items():

        #つぶやき時間がUTCのため、JSTに変換  ※デバック用のコード
        #jsttime = tweet.created_at + datetime.timedelta(hours=9)
        #print(jsttime)

        #つぶやきテキスト(FULL)を取得
        # print(tweet.id_str)
        # print(tweet.created_at)
        # print(tweet.full_text)
        # print(tweet.metadata)
        print(tweet.user.id)
        # print(tweet.user.name)
        # print(tweet.user.description)
        # print(tweet.user.screen_name)
        print(tweet.user.profile_background_image_url)
        pbg = tweet.user.profile_background_image_url
        if pbg!=None:
            ppbg = pbg.split("/")
            extpbg = ppbg[-1].split(".")#拡張子
            print("@"+tweet.user.screen_name+"."+extpbg[1])
            # download_file(pbg,'./images/@'+tweet.user.screen_name+"_pbg."+extpbg[1])


        print(tweet.user.profile_image_url)
        pp = tweet.user.profile_image_url
        if pp!=None:
            ppp = pp.split("/")
            extppp = ppp[-1].split(".")#拡張子
            print("@"+tweet.user.screen_name+"."+extppp[1])
            # download_file(pp,'./images/@'+tweet.user.screen_name+"_pp."+extppp[1])

        print(tweet.user.name)
        print(tweet.user.description)
        tweets_data.append(tweet.full_text + '\n')

        break


    list = api.user_timeline()
    for item in list:
        # print(item.entities)
        # print(item.entities['hashtags'])
        # print(item.entities['user_mentions'])
        # print(item.entities['urls'])

        if 'media' in item.entities:
            # print(item.entities['media'])
            print(item.entities['media'][0]['media_url_https'])
        # print('\n')


    # followers_list = api.followers('bluedqmj3pm')
    #
    # for follower in followers_list:
    #     # friends_count : フォロー数
    #     # followers_count : フォロワー数
    #     # description : 概要（自己紹介が書かれているやつ）
    #     print(follower.screen_name)

    # #出力ファイル名
    # fname = r"'"+ dfile + "'"
    # fname = fname.replace("'","")
    #
    # #ファイル出力
    # with open(fname, "w",encoding="utf-8") as f:
    #     f.writelines(tweets_data)
    # print(tweets_data)


if __name__ == '__main__':

    api = getApiInstance()

    #検索キーワードを入力  ※リツイートを除外する場合 「キーワード -RT 」と入力
    # print ('====== Enter Serch KeyWord   =====')
    # keyword = input('>  ')


    # #出力ファイル名を入力(相対パス or 絶対パス)
    # print ('====== Enter Tweet Data file =====')
    # dfile = input('>  ')

    # gettwitterdata('金色ステッカー')
    # Myfollowing(keyword = '金色ステッカー',api = api)
    Myfriends(keyword = '金色ステッカー',api = api)
