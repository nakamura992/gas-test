import http.client
import json

# APIのホストとエンドポイント
host = "script.google.com"
endpoint = "/macros/s/AKfycbzVQ6mVlOSY5wVXwNprXjRhDF6kgsbuYNM-ZYO2KBvNjMwqOQ91IH4y3eP9uLS8YfMn/exec"

# HTTPクライアントを作成
conn = http.client.HTTPSConnection(host)

try:
    # GETリクエストを送信
    conn.request("GET", endpoint)
    
    # レスポンスを取得
    response = conn.getresponse()
    
    # ステータスコードを確認
    if response.status == 200:
        print("フェッチに成功しました。")
    else:
        print(f"エラーが発生しました: {response.status}")
    
except Exception as e:
    print(f"リクエスト中にエラーが発生しました: {e}")
finally:
    # 接続を閉じる
    conn.close()
