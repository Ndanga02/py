#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#PROBLEM 1
def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 ==0:
        return min(a,b)
    else:
        return max(a,b)


# In[ ]:


#problem 2
def words(arg):
    arg = arg.split()
    
    return arg[0][0] == arg[1][0] 
    
        
        


# In[ ]:


#problem 3
def twenty(*arg):
    return 20 in arg or sum(arg) == 20


# In[ ]:


#problem 4
def old_macdonald(name):
        first_letter = name[0].upper()
        fourth_letter = name[3].upper()
        
        return  first_letter + name[1:3] + fourth_letter + name[4:]


# In[ ]:


#problem 5
def master_yoda(word):
    return word[::-1]


# In[ ]:


#problem 5
def almost_there(number):
    return number in range(190,211) or number in range(90,111) 


# In[ ]:


#problem 6

def has_33(nums):
    for number in range(len(nums) - 1):
        if nums[number] == 3 and nums[number + 1] == 3:
            return True
    


# In[ ]:


#problem 7
def paper_doll(text):
    text.split()
    index_c = 0
    length = len(text)-1
    newtext = ""
    while index_c <= length:
        newtext += text[index_c] * 3
        index_c += 1
        
    print(newtext.capitalize())    
    


# In[ ]:


#problem 8
def blackjack(a,b,c):
    if (not a < 0 and a<=11) and (not b < 0 and b<=11) and (not c < 0 and c<=11):
        if a + b + c <=21:
            return a + b + c
        
        elif a + b + c>21 and 11 in (a,b,c):
            answer = a + b + c - 10
            
            return answer
       
        elif a + b + c > 21:
            return 'BUST'
            
             
       
            
    else:
        return False


# In[ ]:


#problem 9
def summer_69(array):
    ignore = False
    total_sum = 0

    for num in array:
        if num == 6:
            ignore = True
        elif num == 9:
            ignore = False
        elif not ignore:
            total_sum += num

    return total_sum


# In[ ]:


#problem 10
def spy_game(array):
    empty_array = []
    desired_outcome = [0,0,7]
    
    
    for number in array:
        if len(desired_outcome) > len(empty_array) and number == desired_outcome[len(empty_array)]:
            empty_array.append(number)
           
       
    return desired_outcome == empty_array
   
        


# In[27]:


#problem 11
def count_primes(number):
    primes = [2]
    x = 3
    
    while x<=number:
        for y in range(3,x,2):
            if x%y == 0:
                x+=2
                break
        else:
            primes.append(x)
            x+=2
    print(len(primes))


# In[28]:


count_primes(100)


# In[ ]:


2 % 0


# In[20]:


def pop(num):
    array = ['x',7,0,0]
    
    for i in num:
        if i == array[-1]:
            array.pop()
            
    return array == ['x']


# In[31]:


def print_big(letter):
    stars = {1:'  *  ',2:'*****',3:'*    ',4:'      *',5:'       *',6:' *  * ',7:'*    *',8:'     *'}
    letters = {'A':[1,6,7,2,7,7],'B':[2,7,7,6,7,7,2],'C':[2,3,3,2]}
    
    print (stars[letters[letter]])


# In[32]:


print_big('A')


# In[ ]:




