#!/usr/bin/env python
# coding: utf-8

# In[10]:


number= int(input( " enter the intger value:"))
for i in range(number):
    for j in range(i+1):
        print("#", end=" ")
    print()
for i in range(number):
    for j in range(i, number):
        print("#", end=" ")
    print()
            


# In[13]:


word=input(" enter the word:")
reverseWord=""
for ch in word:
    reverseWord=ch+reverseWord
print(" the reverse word is"+reverseWord+"")


# In[ ]:




