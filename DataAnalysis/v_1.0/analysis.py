#!/usr/bin/python
#coding=utf-8
import sys
import pickle
from collections import Counter

data = pickle.load(open("data.pkl", "r"))
data = data.split("\n")

data_count = Counter(data)

for k,v in data_count.iteritems():
    print k, ' 问题出现', v , '次.'

