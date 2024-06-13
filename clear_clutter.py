import os
print(os.getcwd())


def clear(file_type):
    files=(os.listdir("C:\code_fun\python new\Clear_clutter"))
    i=1
    for file in files:
        # print(i)
        if(file.endswith(file_type)):
            if(not os.path.exists(f"C:\code_fun\python new\Clear_clutter\{i}.{file_type}")):
                os.rename(f"C:\code_fun\python new\Clear_clutter\{file}",f"C:\code_fun\python new\Clear_clutter\{i}.{file_type}")
                i=i+1

clear("png")

# for PDFs 

def clear(file_type):
    files=(os.listdir("C:\code_fun\python new\Clear_clutter"))
    i=11
    for file in files:
        # print(i)
        if(file.endswith(file_type)):
            if(not os.path.exists(f"C:\code_fun\python new\Clear_clutter\{i}.{file_type}")):
                os.rename(f"C:\code_fun\python new\Clear_clutter\{file}",f"C:\code_fun\python new\Clear_clutter\{i}.{file_type}")
                i=i+1

clear("pdf")

