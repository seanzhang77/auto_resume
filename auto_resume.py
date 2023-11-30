# author: seanzhang77

##########################################
# 在下面对应填入qBit的WebUI的网址、用户名、密码
##########################################
downloaders = [
    {
        'url': 'https://127.0.0.1:8085/', 
        'username': 'xxx',
        'password': 'xxx'
    },
    {
        'url': '', 
        'username': '',
        'password': ''
    },
    {
        'url': '', 
        'username': '',
        'password': ''
    },
    # 可以继续加，复制上面的格式就行；用不上3个的空着也没事
]

##########################################
# 只需要改上面的，下面的不用动
##########################################

# see https://pypi.org/project/python-qbittorrent/
# pip install python-qbittorrent
from qbittorrent import Client
import warnings
warnings.filterwarnings("ignore")

for dl in downloaders:
    if dl['url'].strip():
        try:
            qb = Client(dl['url'], verify=False)
            qb.login(dl['username'], dl['password'])
            print("login successful to", dl['url'])
        except:
            print("login failed to", dl['url'])
            continue

        lis = qb.torrents(filter='paused')
        if len(lis) == 0:
            print("no waiting seeds")
        for t in lis:
            if t['progress'] == 1:
                print("resume: ", t['infohash_v1'])
                qb.resume(t['infohash_v1'])


