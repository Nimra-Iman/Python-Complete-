import PyPDF2 as p
import os
# !!!!!!!!!!!!!!!!  MERGING PDF FILES  !!!!!!!!!!!!!!!!!!!!!!
merge=p.PdfMerger()
list=os.listdir("C:\code_fun\python new")
for files in list:
    if(files.endswith(".pdf")):
        print(files)
        merge.append(files)
merge.write("combined.pdf")

# !!!!!!!!!!!!!!!!  READING all pages of PDF FILE  !!!!!!!!!!!!!!!!!!!!!
read=p.PdfReader("1.pdf")
text=""
for i in range(len(read.pages)):
    page=read.pages[i]
    t=page.extract_text()
    text=text+t
# print(text)

# !!!!!!!!!!!!!!!!  Reading one/last page of pdf file  !!!!!!!!!!!!!!!!!!!
read_last=p.PdfReader("1.pdf")
te=""
reads=read_last.pages[(len(read.pages)-1)] #length 5 pages ki h to last index "4" hui
tex=reads.extract_text()
te=te+tex
# print(te)

# !!!!!!!!!!!!!!  Adding Password to PDF file  !!!!!!!!!!!!!!!!!!!!!!!
read=p.PdfReader("1.pdf")
writer=p.PdfWriter()
for i in range(len(read.pages)):
    all_pages=read.pages[i]
    writer.add_page(all_pages)
writer.encrypt("superSecret")
writer.write("new_password_vali_file.pdf")

