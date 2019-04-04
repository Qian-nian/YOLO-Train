from voc_eval import voc_eval
import _pickle as cPickle

rec,prec,ap = voc_eval('/home/z840/tensorflow_mode/YOLO/darknet/results/{}.txt','/home/z840/tensorflow_mode/YOLO/darknet/xml_val/{}.xml','/home/z840/tensorflow_mode/YOLO/darknet/data/val-list.txt','dachicun','.')

print('rec:',rec)
print('prec',prec)
print('ap',ap)
