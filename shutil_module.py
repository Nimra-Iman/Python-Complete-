# The name "shutil" is short for shell utility. It provides a convenient and efficient
#  way to automate tasks that are commonly performed on files and directories. 

import shutil
shutil.copy("del.py","delete.py") #yani del.py m jo kuch bhi h vo copy kr k delete.py
# m paste kr do, agar delete.py file ply s h to us k ander jo kuch bhi likha ho ga to new
# any vala data pichly data ko overwrite kr de ga, yani pichla likha hua data chla jay ga

shutil.copy2("del.py","delete.py") #copy2 bhi same copy ki trah hi kaam krta h, but
# meta data ko bhi saath copy krta h 

# to copy ful folder along with its all files
shutil.copytree("C:/Users/J11/Downloads/Documents","C:/Users/J11/Downloads/mydocs")

shutil.move("C:/Users/J11/Downloads/folder 1","C:/Users/J11/Downloads/Documents") #move folder
shutil.move("C:/Users/J11/Downloads/Documents/folder 1/1","C:/Users/J11/Downloads") #move file

# to delete a folder:
shutil.rmtree("C:/Users/J11/Downloads/mydocs")
# to delete a file(shutil can't work):
import os
os.remove("delete.py")

