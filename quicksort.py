#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 09:59:58 2019

@author: mengxiangyu
"""

def quick_sort(array,l,r):
    if l < r-1:
        q = parition(array,l,r);
        quick_sort(array,l,q-1);
        quick_sort(array,q+1,r);
    

    
def parition(array,l,r):
    p = array[l];
    i = l+1;
    for j in list(range(l+1,r)):
        if array[j] > p:
            continue;
        else:
            array[i],array[j] = array[j],array[i];
            i = i+1;
    array[l],array[i-1] = array[i-1],array[l];
    return i-1;
    
                    
            