#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  9 13:22:18 2022

@author: admin
"""
from matplotlib import pyplot as plt
import os
import re
import pandas as pd
import string
from collections import Counter
from scipy.special import kl_div
import numpy as np



import numpy as np
from scipy.stats import norm
from matplotlib import pyplot as plt
import tensorflow as tf
import seaborn as sns
sns.set()


def 1_grams():
    books = dict()
    zipfs = dict()
    zipf_probs = dict()
    for fname in os.listdir('books/stein'):
        if fname != '.DS_Store':
            with open("books/stein/"+fname, 'r') as file:
                lines = file.readlines()
            book = fname.split('.')[0]
            words = []
            for line in lines:
                line = line.translate(str.maketrans('', '', string.punctuation+'”“’')).lower()
                words+= line.split()
            books[book] = words
            counter = Counter(words)
            counts = list(counter.values())
            counts.sort(reverse=True)
            count_count = Counter(counts)
            count_prob = {key:count_count[key]/len(counts) for key in count_count}
            zipf = [(i+1, counts[i]) for i in range(len(counts))]
            zipf_log = [(np.log10(i+1), np.log10(counts[i])) for i in range(len(counts))]
            zipfs[book]=zipf
            zipf_probs[book] = list(count_prob.items())
            plt.plot(list(zip(*zipf_log))[0], list(zip(*zipf_log))[1], label=fname[:-4])
    plt.legend()
   
    books = dict()
    zipfs = dict()
    zipf_probs = dict()
    for fname in os.listdir('books/other'):
        if fname != '.DS_Store':
            with open("books/other/"+fname, 'r') as file:
                lines = file.readlines()
            book = fname.split('.')[0]
            words = []
            for line in lines:
                line = line.translate(str.maketrans('', '', string.punctuation+'”“’')).lower()
                words+= line.split()
            books[book] = words
            counter = Counter(words)
            counts = list(counter.values())
            counts.sort(reverse=True)
            count_count = Counter(counts)
            count_prob = {key:count_count[key]/len(counts) for key in count_count}
            zipf = [(i+1, counts[i]) for i in range(len(counts))]
            zipf_log = [(np.log10(i+1), np.log10(counts[i])) for i in range(len(counts))]
            zipfs[book]=zipf
            zipf_probs[book] = list(count_prob.items())
            plt.plot(list(zip(*zipf_log))[0], list(zip(*zipf_log))[1], label=fname[:-4])
    plt.legend()
        








     

def two_grams():
    books = dict()
    zipfs = dict()
    zipf_probs = dict()
    for fname in os.listdir('books/stein'):
        if fname != '.DS_Store':
            with open("books/stein/"+fname, 'r') as file:
                lines = file.readlines()
            book = fname.split('.')[0]
            words = []
            for line in lines:
                line = line.translate(str.maketrans('', '', string.punctuation+'”“’')).lower()
                words+= line.split()
            two_grams=[]
            for i in range(len(words[:-1])):
                two_grams += [words[i]+' '+words[i+1]]
            books[book] = words
            counter = Counter(two_grams)
            counts = list(counter.values())
            counts.sort(reverse=True)
            count_count = Counter(counts)
            count_prob = {key:count_count[key]/len(counts) for key in count_count}
            zipf = [(i+1, counts[i]) for i in range(len(counts))]
            print(sorted(list(counter.items()), key=lambda x: x[1], reverse=True)[:10])
            zipf_log = [(np.log10(i+1), np.log10(counts[i])) for i in range(len(counts))]
            zipfs[book]=zipf
            zipf_probs[book] = list(count_prob.items())
            plt.plot(list(zip(*zipf_log))[0], list(zip(*zipf_log))[1], label=fname[:-4])
    plt.legend()

