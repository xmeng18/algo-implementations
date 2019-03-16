#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 11:15:46 2019

@author: mengxiangyu
"""
import random as rd
    
def parition_random(array,r):
    k = rd.choice(array);
    rind = array.index(k);
    array[0],array[rind] = array[rind],array[0];
    p = array[0];
    print(p)
    i = 1;
    for j in list(range(1,r)):
        if array[j] > p:
            continue;
        else:
            array[i],array[j] = array[j],array[i];
            i = i+1;
    array[0],array[i-1] = array[i-1],array[0];
    return i-1;

def rand_select(array,order):
    if len(array)== 1:
        return array[0];
    j = parition_random(array,len(array));
    if j == order:
        return array[j];
    elif j>order:
        return rand_select(array[:j],order);
    elif j<order:
        return rand_select(array[j+1:],order - j-1);

