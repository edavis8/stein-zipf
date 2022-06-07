#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 10:38:29 2021

@author: admin
"""
from collections import Counter
from matplotlib import pyplot as plt

#get the words from Ulysses
with open('books/James Joyce___Ulysses.txt') as file:
    words = [word for line in file.readlines() for word in line.strip().split()]

#count the words    
count = sorted(Counter(words).items(), key = lambda x: x[1], reverse=True)

#rank the words
rank_count = list(zip(*[(i+1, count[i][1]) for i in range(len(count))]))

#plot
plt.loglog(rank_count[0],rank_count[1], linestyle='none', marker='o', fillstyle = 'none')

#labels
plt.xlabel('Rank')
plt.ylabel('Frequency')
