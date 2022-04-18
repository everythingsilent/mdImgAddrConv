import requests
import json
import re
import sys

def getRet(local_url:str)->str:
    '''
        get php api return value
    '''
    page = requests.get(r'http://localhost:2727/upload.php?url={}'.format(local_url))
    net_url = json.loads(page.text)['return']
    return net_url


def reWrite(md_url:str)->None:
    with open(md_url,'r',encoding='utf-8') as f:
        text = f.readlines()
        f.close()

    with open(md_url,'w',encoding='utf-8') as f:
        for i in range(len(text)):
            try:
                reg = re.match(r"(\!\[\]\([^>]+?\))",text[i]).span()
                url = text[i][reg[0]+4:reg[1]-1]
                ret = getRet(url)
                print(url,ret)
                f.write("![](http://{})".format(ret))
            except:
                f.write(text[i])
        f.close()

# md_url = r'E:\mdImgAddrConv\README1.md'
reWrite(sys.argv[1])
