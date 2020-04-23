import tweepy
import datetime
import os
import pprint
import time
import urllib.error
import urllib.request

# ツイッターの四字熟語の奴をもらう

def getApiInstance(): #apiを一貫して使うためのものこれをいじることはない

    Consumer_key = 'PpC1XL0KswKbq1lHUE6g4kkPA'
    Consumer_secret = 'HuTx1G1uxKiGyzu6AvzF2PQpcSrAxvlDGy7dSKsFeWHJ84yezT'
    Access_token = '1000380378312404994-3xf6YHeoR8swL7PIVOUm80UtQih06W'
    Access_secret = 'hT22RZjMpEeBDlmiAHmqEzGng8hk8VcBptRhcWWZpHD5b'

    #認証
    auth = tweepy.OAuthHandler(Consumer_key, Consumer_secret)
    auth.set_access_token(Access_token, Access_secret)

    api = tweepy.API(auth, wait_on_rate_limit = True)

    return api

if __name__ == '__main__':

    api = getApiInstance()
    jukugolist = []
    with open("file.txt", mode='w',encoding="utf-8") as f:
        for i in range(100):
            list = api.user_timeline("yjmaniacbot",count=200, page=i+1)
            for item in list:
                txt = item.text
                txt = txt.replace("\n","")
                txt = txt.replace("　","")
                txt = txt.replace("【","")
                txt = txt.replace("】","\t")
                txt = txt.replace("読み：","")
                txt = txt.replace("意味：","\t")
                txlist = txt.split("\t")
                # print(txt.split(","))
                if not txlist[0] in jukugolist:
                    print(txlist[0])
                    jukugolist.append(txlist[0])
                    f.write(txt+"\n")
                else:
                    print("もう入っています")
    
