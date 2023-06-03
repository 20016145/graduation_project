import json
import re
import time
import uuid

import requests

class Image(object):
    def __init__(self,text):
        # URL
        pn = 1
        self.url = f'https://image.baidu.com/search/acjson?tn=resultjson_com&logid=11751424728386358333&ipn=rj&ct=201326592&is=&fp=result&fr=&word={text}&queryWord={text}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&expermode=&nojc=&isAsync=&pn={pn}&rn=30&gsm=1e&1682582894341='
        self.headers = {
            'Cookie': 'BIDUPSID=720D6051B71D92558E908D2E3416E21D; PSTM=1680073085; BAIDUID=720D6051B71D92558224B3D8CF9586CA:FG=1; BAIDUID_BFESS=720D6051B71D92558224B3D8CF9586CA:FG=1; ZFY=QQdwuc5R1HdtqEeRn3mOXus3LSImNfZoMIpVpPFI7S0:C; __bid_n=187c16475d02a6d5424207; FPTOKEN=SlkVDyGPp5mR3GopvUSA4MFdgmOY9ANqyMgT8/Ht44JXxQ/H54x/3J2BlvfHj4w8E+z6Fal7zB1K+EvvSItCYmgsYgfPOeP5peaS3x0hVQiJq+5EKHDBsE9m7A17ih2LxgA/ZfdFvYZ4Hqw36R2kL2oAO6Mx+ZdxurR2MZpuL5y7XnN8Y6jlvOzt3jaGmEFvqkg/VRW6zG1c078x3yHrooZ/jIm4n9SeOdQCMnCFU/7P3ziyXa3F2bITjmE8ldt7dXTlFxsshmP1Cv9Tb3f8T9Qgu2rGudLmS7G80RDTY7/DrGT/3+BcXBKQkDzerC9eKf8WoMeQS8N5XgsJ424wgxsuZ24uwipvK5U3Vq/lC4DmzekCInBCVdy9fGVf1m0UWCJVjSn2YRleL/3+p0jU3g==|rmUcWPCIwYG22qSJqKhxTq61kRa3IKRMnrlpBDDsVs0=|10|4d08b960d5926913c7de2756b5b1caa9; BDRCVFR[X_XKQks0S63]=mk3SLVN4HKm; userFrom=null; firstShowTip=1; indexPageSugList=%5B%22red%22%5D; cleanHistoryStatus=0; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; ab_sr=1.0.1_MDlkNDQ1MWRkMjQyMmM1Y2RjZDU2OWJiOTA5ZWU1Y2U1NTgxOGUxY2FlYWQ0MmQ1MGQ1NmUwN2UyNTVlZDRjNGZjMGEwY2YwNWM1YTYzZWM3Nzk1OTU4MmE3Nzk4ZThhMzdlOTI4OGE3NWZkMmY2Yjc4NWRlZmE5YjU4Nzg0YTc3NzNjZjc1OWUzODg0YjFmNWQ3NmVjZjBkZDk4NWE2Yg==; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
        }
        self.image_list = []
    def get_image(self):
        response = requests.get(url=self.url, headers=self.headers)
        print(json.loads(response.text)['data'][0]['thumbURL'])
        self.image_list.append(json.loads(response.text)['data'][0]['thumbURL'])
        print(self.image_list)

    def save_image(self):
            stuuid = str(uuid.uuid1()).replace("-",'')
            image = requests.get(url=self.image_list[0])
            with open('./static/img/{}.jpg'.format(stuuid), 'wb') as f:
                f.write(image.content)
            return stuuid
def contents(kw):
    url = 'http://kyqn1sf.nat.ipyingshe.com'
    header = {
        "Content-Type": "application/json",
    }
    data = {
        "prompt": kw,
        "history": []
    }
    data = json.dumps(data)
    res = requests.post(url, data=data, headers=header)  # ,headers=header
    resc = json.loads(res.text)
    return resc["response"].strip()



