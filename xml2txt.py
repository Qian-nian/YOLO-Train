import xml.dom.minidom
import os
import numpy as np


def xml2txt(save_dir,srcname):
    #存储目录和原文件名称
    #srcname = filename.split('.')[0] + '.xml'
    savename = srcname.split('.')[0] + '.txt' #获取与图片名相同的的txt文件名
    f = open(os.path.join(save_dir, savename), 'w')#打开txt文件

    DOMTree = xml.dom.minidom.parse('/home/z840/tensorflow_mode/YOLO/darknet/xml_val/' + srcname) #解析xml文档
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
    loc = [] #创建存储位置信息的空列表

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
            a = [objid,x,y,w,h]
            loc.append(a)

    m = np.shape(loc)[0]
    n = np.shape(loc)[1]

    for i in range(m):
        for j in range(n):
            f.write(str(loc[i][j])+' ')
        f.write('\n')
    f.close()

def Test():
    save_dir = '/home/z840/tensorflow_mode/YOLO/darknet/dataset'
    srcname = '1494523489079-ganta.xml'
    xml2txt(save_dir,srcname)


#Test()
save_dir = '/home/z840/tensorflow_mode/YOLO/darknet/traindata'  
if not os.path.exists(save_dir):
    os.mkdir(save_dir)

readfiles = os.listdir('/home/z840/tensorflow_mode/YOLO/darknet/xml_val') #获取xml文件列表
for readfile in readfiles:
    xml2txt(save_dir,readfile)



''' 
save_dir = '/home/z840/tensorflow_mode/YOLO/darknet/dataset'  
if not os.path.exists(save_dir):
    os.mkdir(save_dir)
f = open(os.path.join(save_dir, 'landmark.txt'), 'w')
 
DOMTree = xml.dom.minidom.parse('D:\plate_train\label\Drivingrecord_001.xml')
annotation = DOMTree.documentElement
 
filename = annotation.getElementsByTagName("filename")[0]
imgname = filename.childNodes[0].data+'.jpg'
print(imgname)
   
objects = annotation.getElementsByTagName("object")
 
loc = [imgname]  #文档保存格式：文件名 坐标
 
for object in objects:
    bbox = object.getElementsByTagName("bndbox")[0]
    leftTopx = bbox.getElementsByTagName("leftTopx")[0]
    lefttopx = leftTopx.childNodes[0].data
    print(lefttopx)
    leftTopy = bbox.getElementsByTagName("leftTopy")[0]
    lefttopy = leftTopy.childNodes[0].data
    print(lefttopy)
    rightTopx = bbox.getElementsByTagName("rightTopx")[0]
    righttopx = rightTopx.childNodes[0].data
    print(righttopx)
    rightTopy = bbox.getElementsByTagName("rightTopy")[0]
    righttopy = rightTopy.childNodes[0].data
    print(righttopy)
    rightBottomx = bbox.getElementsByTagName("rightBottomx")[0]
    rightbottomx = rightBottomx.childNodes[0].data
    print(rightbottomx)
    rightBottomy = bbox.getElementsByTagName("rightBottomy")[0]
    rightbottomy = rightBottomy.childNodes[0].data
    print(rightbottomy)
    leftBottomx = bbox.getElementsByTagName("leftBottomx")[0]
    leftbottomx = leftBottomx.childNodes[0].data
    print(leftbottomx)
    leftBottomy = bbox.getElementsByTagName("leftBottomy")[0]
    leftbottomy = leftBottomy.childNodes[0].data 
    print(leftbottomy)
    
    loc = loc + [lefttopx, lefttopy, righttopx, righttopy, rightbottomx, rightbottomy, leftbottomx, leftbottomy]
    
for i in range(len(loc)):
    f.write(str(loc[i])+' ')
f.write('\t\n')    
f.close()
'''
