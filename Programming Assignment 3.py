#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1.Write a Python Program to Check if a Number is Positive, Negative or Zero?


# In[ ]:


num = float(input("Enter a number: "))
if num > 0:
   print("Positive number")
elif num == 0:
   print("Zero")
else:
   print("Negative number")


# In[2]:


#2.Write a Python Program to Check if a Number is Odd or Even?


# In[ ]:


# A number is even if division by 2 gives a remainder of 0.
# If the remainder is 1, it is an odd number.

num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))


# In[ ]:


#3.Write a Python Program to Check Leap Year?


# In[ ]:


year = int(input("Enter a year: "))
if (year%400==0)and(year%100==0):
    print(year,"is a leap year")
elif(year%4==0)and(year%100!=0):
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")


# In[ ]:


#4.Write a Python Program to Check Prime Number?


# In[11]:


num = int(input("Enter a number: "))
if num<2:
    print("It is not a prime number")
else:
    for i in range (2,num):
        if num%i==0:
            print("It is not a prime number")
            break
    else:
        print("It is a prime number")


# In[ ]:


#5.Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?


# In[13]:


lower=1
upper=10000
print("Prime numbers between",lower,"and",upper,"are:")
for num in range(lower, upper+1):
    if num>1:
        for i in range(2,num):
            if(num%i)==0:
                break
        else:
            print(num)


# In[ ]:




