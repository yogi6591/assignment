#REGULAR EXPRESSION.

import re

#Que-1.

print('''Extract the user id, domain name and suffix from the following email addresses. \n emails = "zuck26@facebook.com" "page33@google.com""jeff42@amazon.com"\ndesired_output = [('zuck26', 'facebook', 'com'), ('page33', 'google', 'com'), ('jeff42', 'amazon', 'com')]''')
emails = "zuck26@facebook.com page33@google.com jeff42@amazon.com"
#
# p=re.compile(r"\b([a-z0-9]+)@([a-z]+).\b([a-z]+)")
# result=p.findall(emails)
# print(result)


#OR

p=re.compile(r"([a-z0-9]+)@([a-z]+).([a-z]+)\s([a-z0-9]+)@([a-z]+).([a-z]+)\s([a-z0-9]+)@([a-z]+).([a-z]+)")
result=p.match(emails)
print(result)
a=result.group(1)
b=result.group(2)
c=result.group(3)
A=[a,b,c]
d=result.group(4)
e=result.group(5)
f=result.group(6)
B=[d,e,f]
g=result.group(7)
h=result.group(8)
i=result.group(9)
C=[g,h,i]
l=[]
l.append(tuple(A))
l.append(tuple(B))
l.append(tuple(C))
print("\nMy output is--->>",l)
print("\n****************************\n")



#Que-2.

print("Retrieve all the words starting with ‘b’ or ‘B’ from the following text.\n")
text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
q=re.compile(r"\b[Bb][a-z]+")
answer=q.findall(text)
print("My output is-->>",answer)
print("\n****************************\n")



#Que-3.

print("Split the following irregular sentence into words \nsentence = A, very very; irregular_sentence\ndesired_output = A very very irregular sentence\n")
sentence = "A,very very;irregular_sentence"
p=re.sub(r"[^A-Za-z0-9]"," ",sentence)
print("My output is--->>",p)
print("\n****************************\n")



#Que-4.

print('''Clean up the following tweet so that it contains only the user’s message. That is, remove all URLs, hashtags, mentions, punctuations, RTs and CCs. \n
tweet = Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats \n
desired_output = 'Good advice What I would do differently if I was learning to code today''')

tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''
p=re.sub(r"! RT @TheNextWeb:"," ",tweet)
p=re.sub(r"http://t.co/lbwej0pxOd cc: @garybernhardt #rstats","",p)
print("\n my output is--->>",p)



