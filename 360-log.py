import shutil, os, re

path_root = "C:/user/name/Desktop/Kandao" #directory where you will store your folder which will contain the files
#example "C:/user/name/Desktop/Kandao"
directories = range(1,11) # number of photos, second param should be number of photos + 1. example: 10 photos
#move all your photos to path_root. They should be inside no directory.

#método
def receive_files():
  for dir in directories:
    os.mkdirs(os.path.join(path_root, dir))
    for file in os.listdir(path_root):
      move = re.match('\d+{dir}_', file)
      if (move):
        shutil.move(move, f'{path_root}/{dir}')

#run script
receive_files()
