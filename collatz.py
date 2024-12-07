import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.gridspec as gridspec
import networkx as nx
import math
import pydot
from networkx.drawing.nx_pydot import graphviz_layout

"""
Collatz(n) is a function that takes a number as an argument and gives the number of steps a particular
number needs to reach 1 when Collatz conjecture logic is applied.
"""
def collatz(k):
  if k < 2:
    return 0
  count=0
  while k!=1:
     count+=1
     if k % 2 == 0:    # checking if even
       k=k//2 # k//2 : integer division
     else:
       k=3*k+1
  return count

"""
Collatzpath(n) is a function that takes a number as an argument and returns
 a list with all the values encountered in the path to 1. 
"""

def collatzpath(k):
    lt=[]
    while k!=1:
      if k % 2 == 0:    # checking if even
          k=k//2 # k//2 : integer division
          #print("result of even",k)
          lt.append(k)
      else:
        k=3*k+1
        #print("result of odd",k)
        lt.append(k)
    return lt


"""
collatzpath_to_dictionary function takes the range of numbers as input and gives a dictionary 
that numbers as the keys and its collatzpath as corresponding values 
"""
def collatzpath_to_dictionary(a,b):
  diction={}
  for i in range(a,b):
    diction[i]=collatzpath(i)
  return diction

def place(number,plce):
   place_value = number/(10%(plce-1))/plce
   return place_value

"""
graph_unit_place takes a range of number we want the collatzpaths for.
The goal of this function is to give the output has the {node-pair, weight} format that is required 
for the networkx library
For that purpose, the function takes all the collatzpaths and stores the numbers along 
with their successor as a pair. The number of times this pairs occur in all the collatzpaths
get counted and the count is stored as weight.   
"""

# logic for unit's graph
def graph_unit_place(a,b):
  d1={}
  for i in range(a,b):
    d1[i]=collatzpath(i)
  edge_list={}
  pattern_find = {}
  place_list = []
  for v in d1.keys():
      path_list = d1[v]
      for p in path_list:
        place_list.append(place(p,-1))
      pattern_find[v]=place_list
      place_list2=place_list.copy()
      place_list2.pop(0)
      edg= list(zip(place_list, place_list2))
      edge_list[v]=edg
      

  edgeWeights = {}
  for elist in edge_list.values():
    for e in elist:
      weight = 1
      if e in edgeWeights:
        weight = edgeWeights[e] + 1
      edgeWeights[e] = weight

#convert dictionary to list of 3 tuples (n1, n2, count)
  weighted_edge_list =[]
  for i in edgeWeights:
    t = (i[0],i[1],edgeWeights[i])
    weighted_edge_list.append(t)
  return weighted_edge_list


"""
graph_for_numbers a range of number we want the collatzpaths for.
The goal of this function is to give the output has the {node-pair, weight} format that is required 
for the networkx library
For that purpose, the function takes all the collatzpaths and stores the numbers along 
with their successor as a pair. The number of times this pairs occur in all the collatzpaths
get counted. The count is then converted into log(count) for the purpose of scaling. 
This log(count) is stored as weight for the respective pair.  
"""

#logic to create graph with numbers
def graph_for_numbers(a,b):
  d1={}
  for i in range(a,b):
    d1[i]=collatzpath(i)
  edge_path={}
  for v in d1.keys():
      place_list = d1[v]
      place_list2=place_list.copy()
      place_list2.pop(0)
      edg= list(zip(place_list, place_list2))
      edge_path[v]=edg
      

  edgeW = {}
  for elist in edge_path.values():
    for e in elist:
      weight = 1
      if e in edgeW:
        weight = edgeW[e] + 1
      edgeW[e] = weight

  #convert dictionary to list of 3 tuples (n1, n2, count)
  w_edge_list =[]
  for i in edgeW:
    t = (i[0],i[1],math.log(edgeW[i],10))
    w_edge_list.append(t)

  return w_edge_list







