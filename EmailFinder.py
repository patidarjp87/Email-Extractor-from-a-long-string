import re
str1='''

Hey, my name is jaydeeppatidar and my email id is jaydeeppatidar@gmail.com,
And I am learning programming on xxx youtube channel and I have one more
email:"jaydeeppatidar@yahoo.com"
and some more
email id:<17T219@ietdavv.edu.in>

email:"jaydeeppatidar@dt.com" and I have one more patidarjp@student.com
'''
list1=re.findall(r'\w+@\S+\w',str1)
op=open("list_of_ermails.txt","a")

j=1
for i in list1:
    op.write(f"Email{j}:{i}\n")
    j=j+1
op.close()

print(f"Email's are:{list1}")
print(f"Total Email's are:{j-1}")