import glob
import shutil

#destination path
dest_dir = "~/python/des" #changeme
for file in glob.glob(r'~/python/src/files/*.txt'): #changeme
    print(file)
    shutil.copy(file, dest_dir)