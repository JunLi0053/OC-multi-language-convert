import os
import re
from util.langconv import Converter

sourcePath = "/Users/jun/Desktop/Project/缤纷/BrightenMall/BrightenMall/BrightenMall/Modules"
outputPath = "/Users/jun/Desktop/字符串转换/Localizable.strings"
file_contents = []
class FileContent():
    fileName = ''
    contents = []
    def __init__(self, fileName, contents):
        self.fileName = fileName
        self.contents = contents

# 遍历指定目录，显示目录下的所有文件名
def eachFile(filepath):
    files = os.listdir(filepath) #得到文件夹下的所有文件名称
    str = ''
    for file in files: #遍历文件夹
        path = os.path.join(filepath,file)
        if not os.path.isdir(path) : #判断是否是文件夹，不是文件夹才打开
            if os.path.splitext(file)[1] == '.m': 
                f = open(filepath+"/"+file) #打开文件
                str = f.read()
                content = filter(file,str)
                f.close()
                if content:
                    file_contents.append(content)
        else :
            eachFile(path)

def filter(fileName,content):
    p = '@"[^"]*[\u4E00-\u9FA5]+[^"\n]*"'
    filter_contents = re.findall(p, content)
    if len(filter_contents) > 0:
        print('//'+fileName)
        for content in filter_contents:
            print(content)
        return FileContent(fileName,filter_contents)

# 输入多行文字，写入指定文件并保存到指定文件夹
def writeFile(path,files):
    fopen = open(path, 'w+')
    for fileContent in files:
        fopen.write('\n//'+fileContent.fileName+' --'+str(len(fileContent.contents))+'\n')
        for content in fileContent.contents:
            fopen.write('"'+content+'" = "'+tradition2simple(content)+'" //BMLocalizedString(@"'+content+'")\n')
    fopen.close()

def simple2tradition(line):
    #将简体转换成繁体
    line = Converter('zh-hant').convert(line)
    # line = line.encode('utf-8')
    return line

def tradition2simple(line):
    # 将繁体转换成简体
    line = Converter('zh-hans').convert(line)
    # line = line.encode('utf-8')
    return line

if __name__ == '__main__':
    eachFile(sourcePath)
    writeFile(outputPath,file_contents)
 

