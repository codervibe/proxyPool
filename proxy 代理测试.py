# 代理服务器地址
import requests

# proxy = {
#     "http": "http://117.71.133.118:8089",
#     "http": "http://117.71.154.38:8089"
# }
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML,Like Gecko)'
                  'Chrome/120.0.0.0 Safari/537.36'
}
# 要访问的网址
url = "https://zy.xywlapi.cc/qqapi?qq=3164866298"

try:
    # 发送带有代理的 HTTP 请求
    # response = requests.get(url, proxies=proxy)
    response = requests.get(url, headers=header, timeout=5)
    # 打印响应内容
    print("Response Status:", response.status_code)
    print("Response Content:", response.text)
except requests.exceptions.RequestException as e:
    print("Error sending request:", e)