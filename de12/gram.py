import requests
import random

print("=" * 35)
print("        今日の3色コーデ")
print("=" * 35)

# 天気APIから情報を取得
url = "https://api.open-meteo.com/v1/forecast?latitude=35.45&longitude=139.63&current=temperature_2m,apparent_temperature,precipitation,weather_code&daily=precipitation_probability_max&timezone=Asia%2FTokyo"

try:
    data = requests.get(url, timeout=10).json()

    temp = data["current"]["apparent_temperature"]
    code = data["current"]["weather_code"]
    rain = data["daily"]["precipitation_probability_max"][0]

except:
    print("天気を取得できませんでした。")
    exit()

# 天気を日本語に変換
weather_list = {
    0: "晴れ",
    1: "晴れ",
    2: "晴れ・くもり",
    3: "くもり",
    45: "霧",
    51: "小雨",
    53: "小雨",
    55: "小雨",
    61: "雨",
    63: "雨",
    65: "強い雨",
    71: "雪",
    73: "雪",
    75: "雪",
    80: "にわか雨",
    81: "にわか雨",
    82: "強い雨",
    95: "雷雨"
}

weather = weather_list.get(code, "くもり")

print("\n【今日の天気】")
print("天気：", weather)
print("体感温度：", temp, "℃")
print("降水確率：", rain, "%")

# 気分を選択
print("\n【今日の気分】")
print("1：大人っぽく")
print("2：カジュアル")
print("3：やわらかい雰囲気")
print("4：シンプル")

mood = input("番号を選んでね：")

# 気分に合った配色
colors = {
    "1": [
        ["ネイビー", "アイボリー", "ベージュ"],
        ["ブラウン", "ホワイト", "カーキ"],
        ["グレー", "ブラック", "ボルドー"]
    ],
    "2": [
        ["ブルー", "ホワイト", "ベージュ"],
        ["グリーン", "アイボリー", "デニムブルー"],
        ["ネイビー", "グレー", "ホワイト"]
    ],
    "3": [
        ["アイボリー", "くすみブルー", "ベージュ"],
        ["ライトブルー", "ホワイト", "グレー"],
        ["ブラウン", "アイボリー", "ベージュ"]
    ],
    "4": [
        ["ブラック", "ホワイト", "グレー"],
        ["ネイビー", "ホワイト", "グレー"],
        ["ベージュ", "アイボリー", "ブラウン"]
    ]
}

if mood not in colors:
    mood = "4"

# 3色を抽選
selected = random.choice(colors[mood])

print("\n" + "=" * 35)
print("       今日の3色ショッピング")
print("=" * 35)

print("\n今日の3色は……")

for color in selected:
    print("・", color)

# 気温によって服装を提案
print("\n【おすすめの服装】")

if temp >= 28:
    clothes = "半袖・薄手のパンツ"
elif temp >= 23:
    clothes = "半袖・薄手の羽織り"
elif temp >= 18:
    clothes = "長袖シャツ・カーディガン"
elif temp >= 13:
    clothes = "ニット・ジャケット"
elif temp >= 8:
    clothes = "セーター・コート"
else:
    clothes = "厚手のコート・マフラー"

print(clothes)

# コーディネートを完成
print("\n【今日のコーデ完成！】")
print("トップス：", selected[0])
print("ボトムス：", selected[1])
print("バッグ・小物：", selected[2])

if rain >= 50:
    print("\n雨が降る可能性が高いので傘を忘れずに！")

print("\n今日もおしゃれを楽しもう！")
print("=" * 35)