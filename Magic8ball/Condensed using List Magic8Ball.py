#!/usr/bin/env python
# coding: utf-8

# ### Condensed using List Magic8Ball
# random quote generator
# Authored by @ScottW.Davis - Hvy_D


#%%timeit
import random

Answers = ['It is certain', 
           'It is decidedly so', 
           'Yes', 
           'Reply hazy try again', 
           'Ask again later', 
           'Concentrate and ask again',
           'My reply is no', 
           'Outlook not so good',
           'Very doubtful']

print(Answers[random.randint(0,len(Answers)-1)])

