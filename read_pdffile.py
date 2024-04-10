""" extracting the table c
extracting the number of pages
extracting the particular pages
extracting the text only 
extract datas from the password protected files 
"""
import pdfplumber
# read the files here
result = pdfplumber.open('ankush_resume.pdf')
# for i in result.pages:
#     print(i.extract_text())


# converting them into an pdf file to text file 
text=''
for i in result.pages:
    page_text= i.extract_text()
    text= text + page_text  

with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(text)
