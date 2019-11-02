"""
Created on Thu Oct 31 20:59:33 2019

@author: _千年
"""


import xml.dom.minidom
#import os
import numpy as np
from pandas import DataFrame



def xml2excel(save_file,src_root):
    #存储目录和原文件名称
    #srcname = filename.split('.')[0] + '.xml'
    f = open(src_root,'r')
    
    srcnames = f.readlines()
    f.close()
    loc = []
    for srcname in srcnames:
        #savename = srcname.split('.')[0] + '.txt' #获取与图片名相同的的txt文件名
        #f = open(os.path.join(save_dir, savename), 'w')#打开txt文件
        srcname = srcname.replace('JPEGImages','Annotations')
        xml_name = srcname.rsplit('.',1)[0] + '.xml'
        DOMTree = xml.dom.minidom.parse(xml_name) #解析xml文档
        annotation = DOMTree = DOMTree.documentElement
    
        flname = annotation.getElementsByTagName('filename')[0]
        imname = flname.childNodes[0].data#+'.jpg'
        #print(imname)
    
        size = annotation.getElementsByTagName('size')[0]
        Width = size.getElementsByTagName("width")[0]
        width = Width.childNodes[0].data
        width = int(width)
        Height = size.getElementsByTagName("height")[0]
        height = int(Height.childNodes[0].data)
    
        objects = annotation.getElementsByTagName("object")
        #loc = [] #创建存储位置信息的空列表
    
        for object in objects:
            objid = -1
            Name = object.getElementsByTagName("name")[0]
            name = Name.childNodes[0].data
            if name == 'ganta':
                objid = 0
            if name == 'jueyuanzi':
                objid = 1
            if name == 'dachicun':
                objid = 2
            if name == 'daodixian':
                objid = 3
    
            
            bbox = object.getElementsByTagName("bndbox")[0]
    
            xMin = bbox.getElementsByTagName("xmin")[0]
            xmin = float(xMin.childNodes[0].data)
            yMin = bbox.getElementsByTagName("ymin")[0]
            ymin = float(yMin.childNodes[0].data)
            xMax = bbox.getElementsByTagName("xmax")[0]
            xmax = float(xMax.childNodes[0].data)
            yMax = bbox.getElementsByTagName("ymax")[0]
            ymax = float(yMax.childNodes[0].data)
    
            x = (xmin+xmax)/(2.0*width)
            y = (ymin+ymax)/(2.0*height)
            w = (xmax-xmin)/(width)
            h = (ymax-ymin)/(height)
    
            if objid == -1:
                print('Something is wrong,unrecognizable object tag!')
            else:
                a = [imname,width,height,objid,x,y,w,h]
                loc.append(a)
    
        #m = np.shape(loc)[0]
        #n = np.shape(loc)[1]
    
    loc = np.array(loc).T
    print(loc)
    names = loc[0,:]
    widths = loc[1,:]
    heights = loc[2,:]
    objid = loc[3,:]
    objx = loc[4,:]
    objy = loc[5,:]
    objw = loc[6,:]
    objh = loc[7,:]
    #print(type(names))
    print(names)
    
    
    dict_data = {
    'image name':names,
    'image width':widths,
    'image height':heights,
    'object id':objid,
    'object x':objx,
    'object y':objy,
    'object w':objw,
    'object h':objh
    }
    data = DataFrame(dict_data)
    DataFrame(data).to_excel(save_file,sheet_name = '目标统计')
    
xml2excel('./objectAnno.xlsx','./train-list.txt')
