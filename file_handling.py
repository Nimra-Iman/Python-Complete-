# # to open file in reading mode
# # f=open("text_file.txt","r")  #this open() function use two arguments; one is file name 
# # and other is mode in which we want to open file.
# # There are three modes:
# # ---------> r(open file in reading mode) 
#                 # rt(read file in text mode and it is dafault mode)
#                 # rb(read file in binary mode and tis mode is used to open files
#                     # such as img files, jpg files, pdf or exe files)
# # ---------> w(open file in writing mode , write kr k ap jo bhi likho gy sirf vhi cheez file 
# # m a jay gi or phly jo kuch bhi likha tha vo sab khatam ho jay ga)
# #  --------> a(yani append, append kr k jo bhi likho gy to overwrite nhi ho ga bal k phly vala
# # bhi likha rhy ga or jo kuch ab likho gy vo bhi show ho jay ga end p)
# #  --------> x(x mode is create file mode, agar us name ki already exist kry gi 
# # to error ay ga)



# # agar file ko read mode m open kia h to file ko sirf read kr skty ho, write ya 
# # append etc nhi and same is case with write and append; agar file ko "w" ya "a" mode
# # m khola h to us ko ap write hi kr skti ho read nhi

# # "r" mode is default mode

# # agar ap kisi file ko read mode m open kro or vo exist hi na krti ho to error ay ga
# # but ap kisi bhi file ko write mode m open kro or vo file exist bhi na krti ho to 
# # vo file aytomatically ban jay gi or write k zrye likha hua content us file k ander likh
# # dia jay ga

f=open("myfile.txt","r")
print(f.read())
f.close()


f=open("myfile.txt","w")
f.write("nimra iman which is data with .write")
f.close()


f=open("myfile.txt","a")
f.write(" this is new data added via append")
f.close()

# we can use all these via "with" keyword and with "with" keyword you don't need to
# close file 
with open("myfile.txt","r") as f:
    print(f.read())


with open("myfile.txt","a") as f:
    f.write("\nthis is second line\nthis is third line")









# !!!!!!!!!!!!!1    readline(), readlines(), writelines()  !!!!!!!!!!!!!!!!!!!!!!!

# readline() gives only one line 
with open("myfile.txt","r") as f:
    print(f.readline()) #it will read only first line


# when we want to read all lines via readline()
with open("myfile.txt","r") as f:
    while True:
        line=f.readline() 
        print(line)
        if not line:
            break


#    practice example
with open("data.txt","r") as f:
    i=0
    while True:
        i=i+1
        line=f.readline()
        if not line:
            break
        m1=int(line.split(",")[0])
        m2=int(line.split(",")[1])
        m3=int(line.split(",")[2])
        print(f"marks of student {i} in physics = {m1}")
        print(f"marks of student {i} in math = {m2}")
        print(f"marks of student {i} in sst = {m3}")



# readlines() method is used to read the contents of a file line by line and
# return those lines as a list of strings. Each string in the list corresponds
# to a line in the file. 
with open("myfile.txt","r") as f:
    line=(f.readlines())  
    for i in line:
        print(i)



with open("myfile.txt","r") as f:
    list=(f.readlines()[2])
    print(list)  #via readlines() we can access any single line 

# It's worth noting that readlines() reads the entire file into memory,
#  which may not be efficient for extremely large files. 
# For very large files, you might consider alternative methods like 
# iterating through the file using a for loop or reading the file line
#   by line using the readline() method to reduce memory consumption.



# # to get one specific line
with open("myfile.txt","r") as f:
    line=(f.readlines()[1])  
    print(line)



# #                   WRITELINES()
with open ("new_file.txt","w") as f:
    f.write("this is nimra\n")
    f.write("this is iman\n")
    f.write("this is me\n")   #is trah alag alag likhny s behter h k hm log
    # writelines() ko use kr len

with open ("new_file.txt","w") as f:
    list=["this is nimra\n","this is iman\n","this is me"]
    f.writelines(list) #writelines list ki har string ko alag alag lines pr nhi rkhy
    # gi hmy khud hi \n lgana pry ga ; this can also be done like below:

with open ("new_file.txt","w") as f:
    li=["this is nimra","this is iman","this is me"]
    for i in li:
        f.writelines(i+"\n")



# in order to replace one word
with open("myfile.txt","r") as f:
    output=(f.read()) 
new=output.replace("nimra","namra")
with open("myfile.txt","w") as f:
    output=(f.write(new))



    

#           ##########  SEEK()   ###########################################3
# if you want to chnage 6th character of file then you have to read the file, chnage
# sixth characters and write it, it would be very bad practice;;;;; that's why the
# "seek" function is used 
#   seek and teel functions are part of built_in IO module



with open("myfile.txt","r") as f:
    print(f.read(7))  #read first 7 characters/bytes  

with open("myfile.txt","r") as f:
    print(f.read()[4]) #read 4th index only



#                                  SEEK


with open("myfile.txt","r") as f:
    f.seek(10) 
    print(f.read(7)) #seek(10) krny s vo phly 10 ko chory ga or read(7) krny s vo 7
    # characters read kry ga but y 7 characters 1-7 nhi bl k 11-17 hon gy q k hm n 
    # seek(10) kr dia already


#                              TELL

# f.tell() btay ga k hm n kha tak seek kia hua h: this is helpful for large files
with open("myfile.txt","r") as f:
    f.seek(12) 
    print(f.tell()) #yha answer 12 ay ga, yani reading 13th character s start ho gi
    print(f.read(7))

#                           TRUNCATE

with open("truncate.txt","w") as f:
    f.write("nimra iman is gooooodddd")
    f.truncate(5) #is k krny s m n fix kr dia k sirf 5 bytes/characters hi ayn gy sirf
    # mery file m chahy ap f.write() k zrye kitny hi characters daal do
with open("truncate.txt") as f:
    print(f.read())

