import requests


url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=60161831790547636&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=10&w=%E5%AD%99%E7%87%95%E5%A7%BF&g_tk_new_20200303=5381&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0'
res = requests.get(url)
json_music = res.json()
musics = json_music['data']['song']['list']
for music in musics:
    print('name: ' + music['name']);
    print('album ' + music['album']['name'])
    print('time ' + music['time_public'])
    print('href ' + music['url'])
    print('------------------------------')
