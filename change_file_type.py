import os

# changing root directory to Images folder
rootdir = './Images'
os.chdir(rootdir)

# list of folders inside the Images folder
dirrs = []

# adding folder names to dirrs list
curr_dir = os.getcwd()
for root, dirs, files in os.walk('.', topdown=False):
    dirrs.append(dirs)

# removing empty lists and flattening
list2 = [x for x in dirrs if x != []]
flat_list = [item for sublist in list2 for item in sublist]

curr_dir = os.getcwd()
for item in flat_list:
    # updating current directory to subfolder in Image folder
    os.chdir(curr_dir + '/{}'.format(str(item)))

    # changing the file extension of the jpg files in each subdirectory
    for filename in os.listdir(os.getcwd()):
        if filename.endswith(".jpg"): 
            base = os.path.splitext(filename)[0]
            os.rename(filename, base + ".JPEG")


