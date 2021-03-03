#This script was made for the intent of organizing Kandao Obsidian camera files for preprocessing. Your camera might differ, things might have to be tuned :)

import shutil, os, re

path_root = "C:/user/name/Desktop/Kandao"
#directory where you will store folders for each photo group
#example "C:/user/name/Desktop/Kandao"
directories = range(1,11)
# number of photos, second param should be number of photos + 1. example: 10 photos
#move all your photos to path_root. Files should not be inside any folder.
regex = f'0+{dir}_'
#matches the file depending on the folder number it is going to. begins with at least one zero, contains the current group of photos number.
#example 0001_... photos

#method
def receive_files():
  for dir in directories:
    os.mkdirs(os.path.join(path_root, dir))
    for file in os.listdir(path_root):
      move = re.match(regex, file)
      if (move):
        shutil.move(move, f'{path_root}/{dir}')

#run script
receive_files()
