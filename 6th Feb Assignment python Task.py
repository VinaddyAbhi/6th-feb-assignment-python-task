#!/usr/bin/env python
# coding: utf-8

# Q1. Create a function which will take a list as an argument and return the product of all the numbers
# after creating a flat list.
# Use the below-given list as an argument for your function.
# list1 = [1,2,3,4, [44,55,66, True], False, (34,56,78,89,34), {1,2,3,3,2,1}, {1:34, "key2": [55, 67, 78, 89], 4: (45,
# 22, 61, 34)}, [56, 'data science'], 'Machine Learning']
# Note: you must extract numeric keys and values of the dictionary also.
# 
# 

# In[2]:


def product_of_numbers(lst):
    # Flatten the list
    flat_list = []
    for item in lst:
        if isinstance(item, (list, tuple, set)):
            flat_list.extend(item)
        elif isinstance(item, dict):
            for value in item.values():
                if isinstance(value, (int, float)):
                    flat_list.append(value)
            for key in item.keys():
                if isinstance(key, (int, float)):
                    flat_list.append(key)
        else:
            flat_list.append(item)

    # Calculate the product of all the numbers
    product = 1
    for num in flat_list:
        if isinstance(num, (int, float)):
            product *= num

    return product


# In[5]:


list1 = [1,2,3,4, [44,55,66, True], False, (34,56,78,89,34), {1,2,3,3,2,1}, {1:34, "key2": [55, 67, 78, 89], 4: (45,22, 61, 34)}, [56, 'data science'], 'Machine Learning']

print(product_of_numbers(list1))


# Q2. Write a python program for encrypting a message sent to you by your friend. The logic of encryption
# should be such that, for a the output should be z. For b, the output should be y. For c, the output should
# be x respectively. Also, the whitespace should be replaced with a dollar sign. Keep the punctuation
# marks unchanged.
# Input Sentence: I want to become a Data Scientist.
# Encrypt the above input sentence using the program you just created.

# In[7]:


def encrypt_message(message):
    # Convert the message to lowercase
    message = message.lower()

    # Create a dictionary to store the mapping of letters
    mapping = {}
    for i in range(ord('a'), ord('z')+1):
        mapping[chr(i)] = chr(ord('a') + ord('z') - i)

    # Encrypt the message
    encrypted_message = ""
    for char in message:
        if char in mapping:
            encrypted_message += mapping[char]
        elif char == ' ':
            encrypted_message += '$'
        else:
            encrypted_message += char

    return encrypted_message


# In[8]:


input_sentence = "I want to become a Data Scientist."
encrypted_sentence = encrypt_message(input_sentence)
print(encrypted_sentence)

