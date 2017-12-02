#-*- coding: UTF-8 -*-
import os
import datetime
import shutil
import time

path_list = ['In','InCopy','Out']

# 遍历指定目录，显示目录下的所有文件名
def eachFile(filepath):
    pathDir =  os.listdir(filepath)
##    print pathDir
    for allDir in pathDir:
        child = os.path.join(filepath, allDir)
        print child
        if not os.path.isfile(child):
##           print child.decode('gbk') # .decode('gbk')是解决中文显示乱码问题
           bakPath = os.path.join(child,'bak')
           #checkBakPath(bakPath)
           #print bakPath
           processFile(child,bakPath)

#
def processFile(filepath,bakPath):
    pathDir =  os.listdir(filepath)
    i = 0
    #print filepath
    d1 = datetime.datetime.now()
    for allFile in pathDir:
        fn = os.path.join(filepath, allFile)        
        if os.path.isfile(fn):
           ft = os.path.getctime(fn)
           date = datetime.datetime.fromtimestamp(ft)
           delta = d1 - date
##           print delta.days
           if delta.days < 30 :
##               print fn,'ffffffffffff'
               continue
           yyyyMM = date.strftime('%Y%m')
           bakChildPath = os.path.join(bakPath,yyyyMM)
           #print bakPath
           checkBakPath(bakChildPath)
           bakFn = os.path.join(bakChildPath,allFile)
##           print bakChildPath
##           print allFile
           shutil.move(fn,bakFn)
##        i = i+1
##        if i>15:
##            break
 
                        

#
def checkBakPath(filepath):
    if not os.path.exists(filepath):
       os.makedirs(filepath)


       
if __name__ == '__main__' :
    currPath=os.getcwd()
    for p in path_list:        
        f=os.path.join(currPath, p)
        print f
        eachFile(f)


