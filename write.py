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

files_in_current_directory = [f for f in os.listdir('.') if os.path.isfile(f) and f.rfind('.r') != -1]
files_in_current_directory.sort()
print 'files are ',files_in_current_directory



print 'first_chunk_name is ', first_chunk_name
file_prefix = first_chunk_name[ :first_chunk_name.rfind('.r')]
print 'file_prefix is :', file_prefix

output_file_name = file_prefix+'.mp4'
fw = io.FileIO(output_file_name, 'w')
for filename in files_in_current_directory:
    fr = io.FileIO(filename,'r')
    statinfo = os.stat(filename)

    sizeoffile = statinfo.st_size

    data_to_write = fr.read()
    fw.write( data_to_write )

fw.close()
