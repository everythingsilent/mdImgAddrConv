import requests
import json
import re
import time
import sys

API = 'http://file.nullbyte.com.cn/file_save.php'

def json2array(str):
    return json.loads(str)

def upload(file_url):
    file = open(file_url,'rb')
    up_files = {'file':file}
    resp = requests.post(API,files = up_files)
    return 'http://{}'.format(json2array(resp.text)['return'])

def reWrite(md_url:str)->None:

    #read makerdown file container
    with open(md_url,'r',encoding='utf-8') as f:
        text = f.readlines()
        f.close()

    #rewrite makerdown
    with open(md_url,'w',encoding='utf-8') as f:
        for i in range(len(text)):
            try:
                url = re.match(r'(!\[.*\]\(([^)]+?)\))',text[i]).group(2)
                ret = upload(url)
                print(url," | ",ret)
                print("-"*70)
                f.write("![]({})".format(ret))
                time.sleep(1)
            except:
                f.write(text[i])
        f.close()

# md_file = r'C:\Users\BreaKpoint\Desktop\test.md'
# reWrite(md_file)

reWrite(sys.argv[1])