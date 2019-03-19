import xml.dom.minidom
import os
import numpy as np
from shutil import copyfile

def xmlselect(src_dir,des_dir,img_dir,key):
    readfiles = os.listdir(src_dir)
    count = 0
    for readfile in readfiles:
        DOMTree = xml.dom.minidom.parse(src_dir+'\\' + readfile) #解析xml文档,ubuntu系统下路径改为反斜杠
        annotation = DOMTree = DOMTree.documentElement
        
        flname = annotation.getElementsByTagName('filename')[0]
        imname0 = flname.childNodes[0].data#+'.jpg'
        imname = imanme0.split('.')[0]+'.jpg'
        
        objects = annotation.getElementsByTagName("object")
        #print(objects)
        #count = 0
        for object in objects:
            Name = object.getElementsByTagName("name")[0]
            name = Name.childNodes[0].data
            #print(name)
            if name == key:
                count += 1
                try:
                    copyfile(img_dir+'\\'+imname,des_dir+'\\'+imname)
                except:
                    imname = imanme.split('.')[0]+'.JPG'
                    copyfile(img_dir+'\\'+imname,des_dir+'\\'+imname)
                break
                #print(readfile)
                #copyfile(img_dir+'\\'+imname,des_dir+'\\'+imname)
                #copyfile(src_dir+'\\' + readfile,des_dir+'\\'+readfile)
    print(count)
        
xmlselect('I:\\xml_val','I:\\dachicun','I:\\dataset','jueyuanzi')
