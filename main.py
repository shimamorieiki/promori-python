import tweepy
import datetime
import os
import pprint
import time
import urllib.error
import urllib.request
import MeCab
import re
import usedb as db


# 自分がフォローしている人がいいねまたはリツイートした画像のうち自分がいいと思ったやつを取得
# 自分がフォローしている人を見つける


def getApiInstance():

    Consumer_key = 'PpC1XL0KswKbq1lHUE6g4kkPA'
    Consumer_secret = 'HuTx1G1uxKiGyzu6AvzF2PQpcSrAxvlDGy7dSKsFeWHJ84yezT'
    Access_token = '1000380378312404994-3xf6YHeoR8swL7PIVOUm80UtQih06W'
    Access_secret = 'hT22RZjMpEeBDlmiAHmqEzGng8hk8VcBptRhcWWZpHD5b'

    # 認証
    auth = tweepy.OAuthHandler(Consumer_key, Consumer_secret)
    auth.set_access_token(Access_token, Access_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True)

    return api


def gettwitterdata(keyword, api):
    # 検索キーワード設定
    q = keyword
    sinceDate = db.latest_date("tweets")  # この日付以降のツイートを取得する
    # i = 0
    meishi = []
    doushi = []

    # つぶやきを格納するリスト
    # tweets_data =[]

    # カーソルを使用してデータ取得
    for tweet in tweepy.Cursor(api.search,
                               q=q,
                               count=100,
                               tweet_mode='extended',
                               since=sinceDate  # <-追加
                               ).items():

        meishi = []
        doushi = []
        # print(tweet.user.screen_name)
        # print(tweet.user.protected)
        # print(tweet.user.followers_count)
        # print(tweet.user.friends_count)
        # print(tweet.created_at + datetime.timedelta(hours=9))
        # print(tweet.created_at)
        # print(tweet.user.favourites_count)
        strtext = (tweet.full_text.replace("#どうぶつの森", "")
                   .replace("#AnimalCrossing", "")
                   .replace("#ACNH", "")
                   .replace("#NintendoSwitch", ""))
        strtext = re.sub(
            'https?://[\w/:%#\$&\?\(\)~\.=\+\-]+', "", strtext)
        m = MeCab.Tagger("-Ochasen -u ./dic/atsumori20200507.dic")
        for line in strtext.split("\n"):
            for kore in m.parse(line).split("\t\t"):
                # print(kore)
                linelist = kore.split()
                # print(linelist)
                if len(linelist) >= 3:
                    if "-" in linelist[3]:
                        pos = linelist[3].split("-")
                        if pos[0] == "名詞":
                            meishi.append(linelist[2])
                        elif pos[0] == "動詞":
                            doushi.append(linelist[2])

        if len(meishi) != 0 and len(doushi) != 0:
            # print(tweet.full_text)
            if (("求" or "交換" or "譲" or "出" or "お礼", "余") in meishi or
                    ("求める"or"交換する"or"譲る"or"出す"or"頂く"or"いただく"or"余る") in doushi):
                # i = i + 1
                # print("これは交換希望のツイート")
                # print("ユーザー:"+tweet.user.name)
                # print(strtext)
                # print(meishi)
                # print(doushi)

                # 今からここでほしいものと渡すものの特定を行いたい

                u_n = tweet.user.screen_name
                f_t = tweet.full_text
                c_a = str(tweet.created_at)
                t_id = str(tweet.id)

                created_time = (c_a.replace("-", "")
                                .replace(":", "")
                                .replace(" ", ""))
                # print(time)
                arr = [t_id, u_n, created_time, '', '', f_t]
                db.add_db('tweets', arr)


if __name__ == '__main__':

    api = getApiInstance()

    gettwitterdata('#どうぶつの森', api)
