# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 17:09:07 2020

@author: lenovo
"""

import time

localtime = time.asctime( time.localtime(time.time()) )
print ("本地时间为 :", localtime)