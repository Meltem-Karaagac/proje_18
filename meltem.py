#!/usr/bin/env python
# coding: utf-8

# Create a list which consists of int numbers from 1 to 10 using range() function. Sort the numbers of the list in descending order and print the result.
# 

# In[8]:


mylist = ["a", "g", "b"]
mylist.sort()
print(mylist)


# Select and print the vegetables from the following list using indexing and slicing methods. Note that, except from the given list (grocer), your program must consist of a single line of code.
# grocer = ["banana", ["orange", ["apple", "eggplant", "melon", "spinach", "cheese", "leek" ], "water"], "mandarin"]

# In[18]:


grocer = ["banana", ["orange", ["apple", "eggplant", "melon", "spinach", "cheese", "leek" ], "water"], "mandarin"]
print(grocer[1][1][1:3], grocer[1][1][4:])


# Considering the following flowers and colors lists, write the program using .format() and list indexing methods that will print out the text below.
# text = "My two favorite flowers are tulip and rose, two favorite colors are blue and green."
# 

# In[27]:


flowers = [["jasmine", ["lavender", "rose"], "tulip"]]
colors = ["red", ("blue", ["yellow", "green"]), "pink"]
text = "My two favorite flowers are {} and {}, two favorite colors are {} and {}.".format(flowers[0][2], flowers[0][1][1], colors[1][0], colors[1][1][1])
print(text)


# Re-arrange the sentence using the escape sequences from the list using .format() and list indexing methods to get the following output.
# I am 40 years old.
#     I have two children.
#         Data Science is my IT domain.
#         sentence = "I am 40 years old. I have two children. Data Science is my IT domain."
# 

# In[28]:


escapes = ["\n\t", ("\t", "\t\t"), ["\n", "\n\t\t"]]
sentence = "I am 40 years old.{}I have two children.{}Data Science is my IT domain.".format(escapes[0], escapes[2][1])
print(sentence)


# In[29]:


la = ["bir", 'iki', 'uc', 'dort']
nla = list(la)
nla2 = [la]
print(nla)
print(nla2)


# In[30]:


ms = "2020's hard"
nms = list(ms)
nms2 = [ms]
print(nms)
print(nms2)


# In[34]:


nums = [1, 0, 32, 45, 3]
nums.insert(4, 5)
# nums[4]="Stockholm"
nums


# In[ ]:




