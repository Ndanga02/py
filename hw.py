#!/usr/bin/env python
# coding: utf-8

# In[4]:


def vol(rad):
    return (4/3)*(3.142)*((rad)**3)

vol(2)


# In[9]:


def ran_check(num,low,high):
    return num in range(low,high+1)
ran_check(5,2,7)


# In[11]:


def ran_check2(num,low,high):
    if num in range(low,high+1):
        print(f"{num} is in range {low} and {high}")
ran_check2(5,2,7)


# In[36]:


import string

characters = string.ascii_uppercase
characters_lower = string.ascii_lowercase

def up_low(word):
    up = 0
    low = 0
    for char in word:
        
        if char in characters:
                up += 1
        elif char in characters_lower:
            low += 1
    print(f"there are {up} upper and {low} lower chars")
    
            


# In[39]:


up_low('Hello Mr. Rogers, how are you this fine Tuesday?')


# In[42]:


def unique_list(lst):
    return list(set(lst))
unique_list([1,1,1,1,2,2,3,3,3,3,4,5])


# In[64]:


def multiply(numbers):
    global t
    t = 1
    for num in numbers:
        t = t * num
    print(t)    
multiply([6,54,3,23,4])


# In[65]:


'Hello world'[::-1]


# In[102]:


def palindrome(s):
    new = s.replace(' ','')
    
    return new == new[::-1]
palindrome('h el le h')


# In[103]:


def ispangram(str1, alphabet=string.ascii_lowercase):
    newstr = []
    every_letter = [letter for letter in string.ascii_lowercase]
    for letter in str1:
        if letter not in every_letter:
            pass
        else:
            newstr.append(letter.lower())
        
    unique_newstr = list(set(newstr))
    sorted_newstr = sorted(unique_newstr)
    return every_letter == sorted_newstr
ispangram("The quick brown fox jumps over the lazy dog")


# In[ ]:




