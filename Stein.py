#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 17:37:39 2020

@author: admin
"""
from matplotlib import pyplot as plt
import os
import re
import pandas as pd

for book in os.listdir('books'):
    if book != '.DS_Store':
        with open("books/"+book, 'r') as file:
            lines = file.readlines()
            
        words = []
        for line in lines:
            words+= line.split()
            
        from collections import Counter
        
        c = Counter(words)
        
        y = sorted(list(c.values()), reverse=True)
        x = list(range(1, len(y)+1))
        s = pd.Series(y)
        s.index += 1
        s.to_csv('zipf_stein_comparison/'+re.split(" |__", book)[1]+'.csv')
        plt.loglog(x, y, linestyle='none', fillstyle='none', marker = 'o', label = re.split(" |__", book)[1], alpha = 0.6)
        plt.xlabel('rank')
        plt.ylabel('freq')

plt.legend(loc='best')
plt.tight_layout()
        
