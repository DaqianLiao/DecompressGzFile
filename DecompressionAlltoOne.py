#-*-coding:utf-8 -*-
import gzip
import os.path

#获取gz压缩文件中源文件的名称  
def SetFileName():
    filenames = 'simo_log.txt'
    return filenames

#解压单个gz文件
def untar(filepath , txtfilename):
    gz_file_isok = IsokDecompress(filepath)
    if gz_file_isok:
       file = gzip.open(filepath)
       filedata = file.read()
       outfilexls = open(txtfilename, 'ab')
       outfilexls.write(filedata)
       outfilexls.close
       file.close
    else:
        print(filepath + 'That gz_file is broken!')

#gz文件校验
def IsokDecompress(filepath):
    bool_value = True
    try :
        file = gzip.open(filepath)
        file.read()
        file.close
    except Exception:
        bool_value = False
    return bool_value

#解压指定路径下的所有文件
def  DecompressionAllGzFile(log_path):
    for dirpath, dirnames, filenames in os.walk(log_path):
        for filename in filenames:
            if os.path.splitext(filename)[1] == '.gz':
               gzfilepath = os.path.join(dirpath, filename)
               txtfile = SetFileName()
               txtfilepath = os.path.join(dirpath, txtfile)
               untar(gzfilepath,txtfilepath)
               print(dirpath + ': decompress gz file successfully ! ')
            else:
                print(dirpath + ':  There is no gz file')

def main():
    log_path=input('enter a path:')
    #log_path = 'E:\\python_log\\test_gz_file'
    if os.path.exists(log_path):#判断路径是否存在 异常处理1
       DecompressionAllGzFile(log_path)
    else:
        print('path do not exist')
        main()

if __name__ == "__main__":
    main()
