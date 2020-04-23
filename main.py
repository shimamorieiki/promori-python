import tweepy
import datetime
import os
import pprint
import time
import urllib.error
import urllib.request
import MeCab

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






def gettwitterdata(keyword,api):
    #検索キーワード設定
    q = keyword
    i = 0

    #つぶやきを格納するリスト
    tweets_data =[]

    #カーソルを使用してデータ取得
    for tweet in tweepy.Cursor(api.search, q=q, count=100,tweet_mode='extended').items():
        if tweet.created_at < datetime.datetime.now() + datetime.timedelta(hours=8):
            i = i + 1
            # print(tweet.user.name)
            # print(tweet.user.screen_name)
            # print(tweet.user.protected)
            # print(tweet.user.followers_count)
            # print(tweet.user.friends_count)
            # print(tweet.created_at + datetime.timedelta(hours=9))
            # print(tweet.created_at)
            # print(tweet.user.favourites_count)
            # print(tweet.full_text)
            str = tweet.full_text
            m = MeCab.Tagger("-Ochasen")
            for line in str.split("\n"):
                for kore in m.parse(line).split("\t\t"):
                    for item in　kore:
                        linelist = item.split()
                        if len(linelist)>=3:
                            if "-" in linelist[3]:
                                pos = linelist[3].split("-")
                                keitaiso["pos"] = pos[0]
                                keitaiso["pos1"] = pos[1]
                            else:
                                keitaiso["pos"] = linelist[3]
                                keitaiso["pos1"] = ""

                            keitaiso["surface"] = linelist[0]
                            keitaiso["base"] = linelist[2]


            # with open("./text/text.txt", "a",encoding="utf-8") as f:
            #     f.writelines(str)
            if i > 2:
                break


        else:
            print("これどうなの")
            break



if __name__ == '__main__':

    api = getApiInstance()

    gettwitterdata('#どうぶつの森',api)
