# # normalizing the bounding box values to [0,1]
import os
import shutil

import cv2
from tqdm import tqdm


def convert(img_w,img_h, box):
    x = box[0] + (box[2]/2.0)
    y = box[1] + (box[3]/2.0)
    x = x/img_w
    y = y/img_h
    w = box[2]/img_w
    h = box[3]/img_h
    return x,y,w,h

img_dir = 'images/'
txt_dir = 'labels/'

images_files = os.listdir(img_dir)
txt_files = os.listdir(txt_dir)

for image in tqdm(images_files):
    if os.path.isfile(img_dir+image):
        img = cv2.imread(os.path.join(img_dir,image))
        img_h , img_w, _ = img.shape

        fname = image.split('.')[0]
        fname = fname+'.txt'
        txt_file = os.path.join(txt_dir,fname)
        lines =[]
        with open(txt_file) as f:
            for line in f:
                labels = line.split()
                labels[0]= int(labels[0])
                labels[1],labels[2],labels[3],labels[4] = float(labels[1]),float(labels[2]),float(labels[3]),float(labels[4])
                box = [labels[1],labels[2],labels[3],labels[4]]
                labels[1],labels[2],labels[3],labels[4] = convert(img_w,img_h,box)
                new_line = ' '.join(str(i) for i in labels)
                line = line.replace(line,new_line)
                lines.append(line)
            f.close()
        with open(txt_file,'w') as fw:
            for line in lines:
                fw.write(line)
                fw.write("\n")
            fw.close()

# Path to the folder containing text files
folder_path = "duplicateLabels/"

# List all files in the folder
files = os.listdir(folder_path)

# Iterate over each file in the folder
for file_name in tqdm(files):
    # Check if the file is a text file
    if file_name.endswith(".txt"):
        # Remove common image extensions
        for ext in [".png", ".jpg", ".jpeg", ".PNG", ".JPG", ".JPEG"]:
            if ext in file_name:
                new_file_name = file_name.replace(ext, "")
                # Construct the old and new file paths
                old_file_path = os.path.join(folder_path, file_name)
                new_file_path = os.path.join(folder_path, new_file_name)
                # Rename the file
                os.rename(old_file_path, new_file_path)
                break  # Break out of loop once extension is found and replaced



# Source folder containing subfolders with text files
source_folder = "ExDark_Annno/"

# Destination folder to move text files
destination_folder = "duplicateLabels/"

# Recursively traverse each subfolder
for root, dirs, files in os.walk(source_folder):
    # Iterate over each file in the current subfolder
    for file_name in files:
        # Check if the file is a text file
        if file_name.endswith(".txt"):
            # Construct the old and new file paths
            old_file_path = os.path.join(root, file_name)
            new_file_path = os.path.join(destination_folder, file_name)
            # Move the file to the destination folder
            shutil.move(old_file_path, new_file_path)



def read_text_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def compare_text_files(file1_path, file2_path):
    content1 = read_text_file(file1_path)
    content2 = read_text_file(file2_path)
    return content1 == content2

folder1_path = "labels/"
folder2_path = "duplicateLabels/"

folder1_files = [file for file in os.listdir(folder1_path) if file.endswith(".txt")]
folder2_files = [file for file in os.listdir(folder2_path) if file.endswith(".txt")]

for file_name in tqdm(folder1_files):
    file1_path = os.path.join(folder1_path, file_name)
    file2_path = os.path.join(folder2_path, file_name)
    if compare_text_files(file1_path, file2_path):
        print(f"File {file_name} has the same content in both folders.")
