import keyword

file = open('ques6.py','r')

source_code=file.read()
words=source_code.split()
keyword_count=0

for word in words:
    if keyword.iskeyword(word):
        keyword_count+=1
        
print("Total Number of keyword  found in this source file", keyword_count)

file.close()