import os


# !!!!!!!!!!!!!!  CREATING A NEW FOLDER/DIRECTORY   !!!!!!!!!!!!!!!!!!
if(not os.path.exists("new_folder_by_os")): #y if condition y cheeze check krny 
    # k liye lgai h k agar y folder exist nhi krta to bna do, agar exist krta h to
    # of course vo "if" consition k ander hi nhi jay ga, y condition is liye
    # lgai q k first time to code run krny pr y cha pry ga (agar is naam s folder
    # exist na krta hua to) lekin second time run krny pr error de ga q k vo khy 
    # ga k y folder to already bna hua h or doobara isi naam s doosra folder
    # kesy bna du
    os.mkdir("new_folder_by_os")



# !!!!!!!!!!!!!!!!!  CREATING SUB FOLDER INSIDE FOLDER!!!!!!!!!!!!!!!!!!
for i in range(1,11):
    if(not os.path.exists(f"new_folder_by_os/tut{i}")):
        os.mkdir(f"new_folder_by_os/tut{i}")
    # os.mkdir(f"new_folder_by_os/tut{i}/main.py")


# !!!!!!!!!!!!!!!!!!  RENAMING FOLDERS  !!!!!!!!!!!!!!!!!!!!!!!!
for i in range(1,5):
    if(not os.path.exists(f"new_folder_by_os/tut{i}/python.py")):
        os.rename(f"new_folder_by_os/tut{i}/main.py",f"new_folder_by_os/tut{i}/python.py")



#  !!!!!!!!!!!!!!!!!!!!!! LIST OF ALL FOLDERS INSIDE A FOLDER!!!!!!!!!!!!!!!!               
output=os.listdir("new_folder_by_os") 
print(output) 


#   !!!!!!!!!!!!!!! TO GET CURRENT DIRECTORY  !!!!!!!!!!!!!!
print(os.getcwd())


#!!!!!!!!!!!!!!!!!!! TO CHANGE DIRECTORY  !!!!!!!!!!!!!!!!!!!!!
print(os.chdir("C:/Users/J11/Downloads/Documents"))

if(not os.path.exists("new_folder_by_os")):
    os.mkdir("new_folder_by_os") # ab y vala folder "C:/Users/J11/Downloads/Documents"
    # is k ander bny ga 


