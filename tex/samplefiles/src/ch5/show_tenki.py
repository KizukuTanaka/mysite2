# 東京の天気をJSONで取得できるURL --- (*1)
url = "https://api.aoikujira.com/tenki/week.php?fmt=json"
url += "&city=319"

# Webから天気情報を取得する --- (*2)
import urllib.request as req
res = req.urlopen(url)
json_data = res.read()

# JSONデータをPythonのデータ型に変換 --- (*3)
import json
data = json.loads(json_data)

# 結果を表示 --- (*4)
for row in data["319"]:
    date = row["date"]
    forecast = row["forecast"]
    print(date + " : " + forecast)

