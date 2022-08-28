# 天気予報を取得するモジュール
# URLからJSONデータをダウンロードする関数 --- (*1)
def get_json(url):
    import urllib.request as req
    import json
    # データをダウンロード
    res = req.urlopen(url)
    json_data = res.read()
    # JSONデータをPythonで扱えるよう読み込む
    return json.loads(json_data)

# 都市IDを取得することで天気情報を取得する関数 --- (*2)
def get_weather(city_id):
    url = "https://api.aoikujira.com/tenki/week.php?fmt=json"
    url += "&city=" + str(city_id)
    data = get_json(url)
    s = ""
    for row in data[str(city_id)]:
        date = row["date"]
        forecast = row["forecast"]
        s += date + " : " + forecast + "\n"
    return s

# モジュールとして利用されるかどうか判定
if __name__ == "__main__":
    res = get_weather(319) # 東京の天気を取得 --- (*3)
    print(res)

