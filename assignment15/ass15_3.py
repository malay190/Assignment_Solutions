#Q.3- Split the following irregular sentence into words 

import re

sentence = "A, very very; irregular_sentence"

p=re.compile(r"[^A-Za-z0-9]")
result=p.sub(" ",sentence)
 
print(result)