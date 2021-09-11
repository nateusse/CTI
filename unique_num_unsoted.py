#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given an array/list nums containing n unsorted numbers between 
-3 * 104 and 3 * 104  return the only number that appears once in the array/list.

@author: nat
"""



def single(nums):
    xor_out = 0
    for i in nums:
        xor_out = xor_out ^ i;
    return(xor_out)

single([3, 3, 5, 4, 4])