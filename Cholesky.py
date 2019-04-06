#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 16:43:02 2019

@author: mengxiangyu
"""
import numpy as np
import math as m
def cholesky(S):
    n = S.shape[0]
    A = np.zeros((n,n))
    v = np.zeros(n)
    for j in range(n):
        for i in range(j,n):
            v[i] = S[i][j]
            for k in range(j):
                v[i] = v[i] - A[j][k]*A[i][k]
            A[i][j] = v[i]/m.sqrt(v[j])
    return(A)
                
    