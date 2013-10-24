import io
import sys
import os

def get_initial_name(name):
    index = name.rfind('.')
    return name[:index]
def get_chunk_file_name(name,index):
    chunkname = name+'.r'+str(index)
    return chunkname	
kb = 1024
mb = 1024*kb
chunksize = 100*mb
filename = sys.argv[1]

statinfo = os.stat(filename)

sizeoffile = statinfo.st_size

numchunks = sizeoffile/chunksize + 1

prefix = get_initial_name(filename)
print 'init name is ',prefix
print 'numchunks is ',numchunks


fr = io.FileIO(filename,'r')

for i in range(1,numchunks+1):
    chunkfilename =  get_chunk_file_name(prefix,i)
    datatowrite = fr.read(chunksize)
    sizeread = sys.getsizeof(datatowrite)
    print 'sizeread is ', sizeread
    fw = io.FileIO(chunkfilename, 'w')
    fw.write(datatowrite)
    fw.close()
