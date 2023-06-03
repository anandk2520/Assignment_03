#!/usr/bin/env python
# coding: utf-8

# In[2]:


# 1 .What is the difference between set and dictionary,Explain with an example.

"""A set is an unordered collection of unique elements. It does not allow duplicate values.
The elements in a set are not stored in any particular order, 
which means you cannot access elements by their position or index."""

a={1,2,3,4,5}


"""A dictionary (also known as a map or associative array) is an unordered collection of key-value pairs.
Each element in a dictionary consists of a key and its associated value. 
The key acts as a unique identifier for the value, allowing you to retrieve the value using the key."""


b={"brand":"Suzuky","year":1950,"colour":"Black"}



# In[3]:


a


# In[4]:


b


# In[7]:


# 2.Write a program to print the following pattern 
#     *
#     **
#     ***


n=4
for i in range(1,n):
    print("*"*i)
    i=i+1
 
 


# In[10]:


# 3.Write a program to print n natural number in ascending order using a while loop?

n = int(input("Enter the value of n: "))
i= 1

while i <= n:
    print(i)
    i =i+ 1


# In[12]:


# 4.Write a program in Python to swap between two numbers without using a third variable

a= int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("Before swapping: num1 =", a, "num2 =", b)

a = a + b
a = a - b
a = a - b

print("After swapping: num1 =", a, "num2 =", b)


# In[13]:


# 5.How to Create a Function with Default Arguments in Python.( Example)

def greet(name, message="Hello"):
    print(f"{message}, {name}!")


greet("Akash")  

greet("Sam", "Hi")  


# In[17]:


# 6.Display a square of numbers from 1 to 10 using list comprehension.

squared_numbers= [i**2 for i in range(1, 11)]
print(squared_numbers)


# In[18]:


# 7.What is polymorphism? Explain with example( class)

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

rectangle = Rectangle(5, 3)
circle = Circle(7)

print(rectangle.area())  
print(circle.area())  

# 8. Explain conditional probability with example?

Conditional probability :
    conditional probability states that the probability that an event occurs given the knowledge that 
    another event has occurred.
    This is to say that the chance of one event happening is conditional on another event happening.
    
    The probability that you get a six, given that you drew a red card is P(6│red) = 2/26 = 1/13, 
    since there are two sixes out of 26 red cards.
# # 9.Explain Emphirical rule  with diagram .
# 
# The Empirical Rule, also known as the 68-95-99.7 Rule,
# is a statistical concept that provides a guideline for understanding the distribution of data in a normal distribution. 
# The rule states that for a bell-shaped, symmetrical distribution:
# 
# Approximately 68% of the data falls within one standard deviation of the mean.
# Approximately 95% of the data falls within two standard deviations of the mean.
# Approximately 99.7% of the data falls within three standard deviations of the mean
# 
# ![image.png](attachment:image.png)

# In[ ]:


#10. What is Hypothesis Testing ? What is the Role of p value in HT?

HYPOTHESIS TESTING:
        A statistical test is a method of 
        statistical inference used to decide wheather the data at hand sufficiently support a particular hypothesis.
   
        Hypothesis testing allows us to make probabilistic  statements about population
        parameters.
alpha:
    The probability with which we will reject the  null hypothesis, when its true.
    
p-value:
        P value  is the probability of null hypothesis being true.
        
        
        
e.g;   H0=100
       H1!=100
    
       if p < alpha,we reject the null hypothesis.
    


# In[ ]:


# Q 2.List all the probability distributions with example?


1.Uniform Distribution:
     e.g.  Tossing a coin
        
2.Binomial Disribution :
    e.g.   The prediction of the number of spam emails received by a person is one of the prominent examples 
           of a binomial distribution.
           This is because an email has two possibilities, i.e., either it can be a spam e-mail or not.
            
3.Normal Distribution:
    e.g. size of shoes
    
4.Exponential Distribution:
    e.g. life of a car
    
5.POisson Distribution:
    e.g No of customers arrives in bank in a hour

