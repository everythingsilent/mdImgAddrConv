# md图片地址转换

## php api说明

> localToNetAddress //本地地址转换为网络地址
>
> 该php需上传到服务器,作为网络存储设备
### 参数说明

| 传输参数名 | 传输内容         | 传输方式 |
| ---------- | ---------------- | -------- |
| url        | 本地文件绝对路径 | get      |

## main.py说明

```python
import requests
import json
import re
import sys

def getRet(local_url:str)->str:
    '''
    input 需上传的本地文件绝对路径
    return 网络地址
    '''
    page = requests.get(r'http://localhost:80/upload.php?url={}'.format(local_url))
    net_url = json.loads(page.text)['return']
    return net_url


def reWrite(md_url:str)->None:
    '''
   	input makerdown文档的绝对路径
	return none
   	'''
    
    #读取makerdown文档
    with open(md_url,'r',encoding='utf-8') as f:
        text = f.readlines()
        f.close()
	
    
    #遍历makerdown文档的每行
    with open(md_url,'w',encoding='utf-8') as f:
        for i in range(len(text)):
            try:
                #正则表达式进行匹配,不存在则触发错误原行写出,存在则获取网络地址,本地修改成网络地址
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
```



## 如何使用

1. 上传php 文件到服务器
2. 修改python中请求的php api地址
3. cmd命令行中 python main.py makerdown.md
