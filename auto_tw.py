import tweepy


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


if __name__ == "__main__":
    api = getApiInstance()
    api.update_status('自動ツイートできてる？')
