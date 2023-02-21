# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 11:08:13 2023

@author: 1md
"""
import tqdm
import time
##对tqdm库的学习 tqdm库：方便观察处理进度
a=[1,2,3]
for idx, element in enumerate(tqdm.tqdm(a)):
    time.sleep(1)
    print(f"No.{idx}: {element}")
    print(f"No.{idx}: {element}")
    
print("1")
time.sleep(2)
print("ok")