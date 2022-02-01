# import module
import os
 
# assign size
size = 0
 
# assign folder path
Folderpath = '/BACKUP/2ad4e572-afe5-40fe-8afe-4c63e9d17d7a/'
 
# get size
# get size
for ele in os.scandir(Folderpath):
    size+=os.path.getsize(ele)
 
# display size
print("Folder size: " + str(size))