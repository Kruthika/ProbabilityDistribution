# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 23:17:39 2015

@author: Kruthika
"""
import matplotlib.pyplot as plt
import collections
import numpy as np 
import scipy.stats as stats

x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]
c = collections.Counter(x)
print c
# calculate the number of instances in the list
count_sum = sum(c.values())
for k,v in c.iteritems():
  print "The frequency of number " + str(k) + " is " + str(float(v) / count_sum)                     

#To print box plot  
plt.figure()
plt.boxplot(x)
plt.savefig("boxplot.png")

#To print histogram
plt.figure()
plt.hist(x, histtype='bar')
plt.savefig("histogram.png")

#to print QQ normal plot
plt.figure()
test_data = np.random.normal(x)   
graph1 = stats.probplot(test_data, dist="norm", plot=plt)
plt.savefig("qqplot_normal.png")

#To print QQ uniform plot
plt.figure()
test_data2 = np.random.uniform(x)   
graph2 = stats.probplot(test_data2, dist="norm", plot=plt)
plt.savefig("qqplot_unform.png")