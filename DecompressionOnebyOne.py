import gzip
import os.path

#获取gz压缩文件中源文件的名称  
def get_decompress_file_name(filepath):
    filelen = 16#gz中源文件名的长度
    gz = gzip.GzipFile(mode="rb", fileobj=open(filepath, 'rb'))
    gzfile = gz.fileobj
    filehead = gzfile.read(10)
    fname = []
    fname.append(gzfile.read(filelen))
    filename = fname[0].decode('UTF-8')#转化成字符串格式
    if filename[filelen - 1] =='.':
        filename = filename[:-1]
    filenames = filename + '.txt'
    gz.close
    return filenames

#解压单个gz文件
def untar(filepath , txtfilename):
    gz_file_isok = gz_isok_to_decompress(filepath)
    if gz_file_isok:
       file = gzip.open(filepath)
       filedata = file.read()
       outfilexls = open(txtfilename, 'wb')
       outfilexls.write(filedata)
       outfilexls.close
       file.close
    else:
        print(filepath + 'That gz_file is broken!')

#gz文件校验
def gz_isok_to_decompress(filepath):
    bool_value = True
    try :
        file = gzip.open(filepath)
        file.read()
        file.close
    except Exception:
        bool_value = False
    return bool_value

#解压指定路径下的所有文件
def  decompression_gz_all(log_path):
    for dirpath, dirnames, filenames in os.walk(log_path):
        for filename in filenames:
            if os.path.splitext(filename)[1] == '.gz':
               gzfilepath = os.path.join(dirpath, filename)
               txtfile = get_decompress_file_name(gzfilepath)
               txtfilepath = os.path.join(dirpath, txtfile)
               untar(gzfilepath,txtfilepath)
               print(dirpath + ': decompress gz file successfully ! ')
               delfile(filepath) # 删除文件
            else:
                print(dirpath + ':  There is no gz file')

#删除单个文件          
def delfile(fname):
    if os.path.exists(fname):
        os.remove(fname)
        
#多个txt文件组合成一个大txt文件     
def adddatatotxt(filepath , txtname):
    filedata= open(filepath,'rb')
    data=filedata.read()
    txtfile = open(txtname,'ab')
    txtfile.write(data)
    filedata.close
    txtfile.close         
               
def main():
    log_path=input('enter a path:')
    #log_path = 'E:\\python_log\\test_gz_file'
    if os.path.exists(log_path):#判断路径是否存在 异常处理1
       decompression_gz_all(log_path)
    else:
        print('path do not exist')
        main()

if __name__ == "__main__":
    main()

               



