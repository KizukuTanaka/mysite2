# Flickr APIの設定(要書き換え)
key = "928934654********37fd"
secret = "3e********c"

# ライブラリを取り込む
import flickr_downloader as fli

# レモン(lemon)のダウンロード
fli.download("lemon", "./lemon",
        api_key=key, api_secret=secret)
# イチゴ(strawberry)のダウンロード
fli.download("strawberry", "./strawberry",
        api_key=key, api_secret=secret)
print("ok")
