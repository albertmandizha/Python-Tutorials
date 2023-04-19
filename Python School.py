#!/usr/bin/env python
# coding: utf-8

# ## Strings

# In[ ]:


first='John'
last='Smith'
message=first + '['+ last +'] is a coder'
msg= f'{first} {last} is a coder'
print(msg)


# In[ ]:


course='Python for Beginners'
print(len(course)) #to calculate the length of a string
print(course.upper()) # to convert a string from lower to Upper Case
print(course.find('o')) #gives the index of the characters and is case sensitive
print(course.replace('Beginners','Absolute Beginners')) #replacing the characters we can replace the single character
print('Python' in course) #to check if the Python sequence of the string


# ## Arithmetic Operators

# In[ ]:


#Argumented Assignment Operator
x=10
x-=3 #Argumented Assignment Operator
print(x)


# In[ ]:


# Operator Presedence
x= (10 + 3) * 2 ** 2
print(x)
#parathesis and Exponetiation first 2**2, then multiplication or division and addition or subtration


# In[ ]:


# Rounding and Absolute Values
import math
print(math.ceil(2.9))
x=2.9
print(abs(-2.9)) #always return the positive value always


# ## If statements

# In[ ]:


is_hot=False
is_cold= True
if is_hot:
    print('its a hot day')
    print('Drink Plent of water')
elif is_cold:
    print('its a cold day')
    print('wear warm clothes')
    
else:
    print('it is a lovely day')
    print("Enjoy your day")


# In[ ]:


price= 1000000
is_credit_good=True
if is_credit_good:
    down_payment=0.1*price
else:
    down_payment=0.2*price
    
print(f'Down Payment:${down_payment}')
    


# ### Logical Operators in Python

# In[ ]:


has_high_income=True
has_good_credit=False

if has_high_income or has_good_credit:
    print('Eligible for a loan')


# In[ ]:


### Comparison operators
temperature = 35
if temperature >=30:
    print('its a hot day')
else:
    print('its not a hot day')


# In[ ]:


name='john'
if len(name)<3:
    print('name must be atleast 3 characters')
elif len(name)>50:
    print('name can be maximum of 50 characters')
else:
    print ('name looks good')


# In[ ]:


weight=int(input('weight:')) #input always returns a string thats why we had to use the int
unit=input('(L)bs or (K)g:')
if unit.upper()=='L':
    converted = weight *0.45
    print(f'You are {converted} kilos')
else:
    converted=weight/0.45
    print(f'You are {converted} pounds')


# ## While loops

# In[ ]:


# while condition
i =1
while i<=5:
    print('*'*i)
    i=i+1
print('Done')


# In[5]:


##Guesing game
secrete_number =9
gues_count=0
gues_limit=3
while gues_count<gues_limit:
    gues=int(input('Gues:'))
    gues_count+=1
    if gues==secrete_number:
        print('you won!')
        break
else:
    print('Sorry you failed')


# In[ ]:





# In[ ]:




