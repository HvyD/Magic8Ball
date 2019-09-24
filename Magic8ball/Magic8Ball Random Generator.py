#!/usr/bin/env python
# coding: utf-8

# ### Magic8Ball
# random quote generator
# Authored by @ScottW.Davis - Hvy_D

import random

def Ask8Ball(retort):
    if retort == 1:
        return 'It is certain'
    elif retort == 2:
        return 'It is decidedly so'
    elif retort == 3:
        return 'Yes'
    elif retort == 4:
        return 'Reply hazy try again'
    elif retort == 5:
        return 'Ask again later'
    elif retort == 6:
        return 'Concentrate and ask again'
    elif retort == 7:
        return 'My reply is no'
    elif retort == 8:
        return 'Outlook not so good'
    elif retort == 9:
        return 'Very doubtful'
    
    
print(Ask8Ball(random.randint(1,9)))

