import os
import shutil
path = '/media/keshav/Local Disk/study/PHP for Beginners - udemy'

# create a new folder

entries = os.listdir(path)

if(not os.path.exists(os.path.join(path, 'data'))):
    os.mkdir(os.path.join(path, 'data'))

# start reading a folder from folder
for entry in entries:
    if(entry.endswith('.zip')):
        continue
    folders = os.listdir(os.path.join(path, entry))

    for i in folders:
        files = os.listdir(os.path.join(path, entry, i))
        if not os.path.exists(os.path.join(path, 'data', i)):
            os.mkdir(os.path.join(path, 'data', i))
        print(os.path.exists(os.path.join(path, 'data', i)))

        for j in files:
            print(j)
            shutil.copy(os.path.join(path, entry, i, j),
                        os.path.join(path, 'data', i, j))

        # print(files)
    # if there is another folder inside keep track of folder name and get in

    # after getting in check if folder exists in root if yes copy data of folder if not create folder and copy data after
