# train test split
import glob, os

# Current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Directory where the data will reside, relative to 'darknet.exe'
path_data = './images/'
os.chdir(path_data)
new_path = os.getcwd()

# Percentage of images to be used for the test set
percentage_test = 30

# Create and/or truncate train.txt and test.txt
file_train = open('train.txt', 'w')  
file_test = open('test.txt', 'w')

# Populate train.txt and test.txt
counter = 1  
index_test = round(100 / percentage_test)  

temp = os.path.join(current_dir, "*.jpg")

for pathAndFilename in glob.iglob(os.path.join(new_path, "*.jpg")):  
    # print(pathAndFilename)
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))


    if counter == index_test:
        counter = 1
        file_test.write(path_data + title + '.jpg' + '\n')
    else:
        file_train.write(path_data + title + '.jpg' + '\n')
        counter = counter + 1

file_test.close()
file_train.close()
