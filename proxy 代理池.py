import re, requests, queue, threading, time, datetime

Proxy_89 = 'https://www.89ip.cn/index_{}.htmL'
Proxy_KD = 'https://www.kuaidaili.com/free/inha/{}'
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML,Like Gecko)'
                  'Chrome/120.0.0.0 Safari/537.36'
}
filename = (str(datetime.datetime.now()).replace(' ', '-').replace(':', '-').split('.')[0]) + '_存活网址.txt'
# filename = '1000page存活网址.txt'
timename = str(datetime.datetime.now()).split('.')[0]
q = queue.Queue()


def GetContent(url, header):
    try:
        res = requests.get(url, headers=header, timeout=5).content.decode()
        if res != None:
            return res
        else:
            return None
    except:
        return None


def GetProxyIp():
    for i in range(1,200):
        con = GetContent(Proxy_89.format(i), header)
        if con is not None:
            ips = [':'.join(x) for x in
                   re.findall('<td>\n\t\t\t(\d.*?)\t\t</td>\n\t\t<td>\n\t\t\t(\d.*?)\t\t</td>', con)]
            for ip in ips:
                q.put(ip)

        con = GetContent(Proxy_KD.format(i), header)
        if con != None:
            ips = [':'.join(x) for x in
                   re.findall('td data-title="IP">(.*?)</td>.*?data-title="PORT">(.*?)</td>', con, re.S)]
            for ip in ips:
                q.put(ip)


def CheckProxyIp():
    url = 'https://www.baidu.com'
    while not q.empty():
        ip = q.get_nowait()
        proxy = {}
        proxy['http'] = str(ip)
        res = requests.get(url, headers=header, timeout=5, proxies=proxy)
        # if res.status_code == 200 and '百度一下' in res.content.decode():
        if res.status_code == 200:
            print('[{}] 发现免费代理: {}'.format(timename, ip))
            with open(filename, 'a+') as a:
                a.write(ip + '\n')


if __name__ == '__main__':
    print('_________________')
    threading.Thread(target=GetProxyIp).start()
    time.sleep(1)
    for i in range(3):
        threading.Thread(target=CheckProxyIp).start()
