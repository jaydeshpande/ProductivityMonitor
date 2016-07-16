# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 11:39:54 2016

@author: Jaydeep
"""

from datetime import datetime


def gettime():
    A = str(datetime.now())
    B = str.split(A)
    date = int(B[0].split('-')[2])
    month = int(B[0].split('-')[1])
    year = int(B[0].split('-')[0])
    hour = int(B[1].split(':')[0])
    minute = int(B[1].split(':')[1])
    second = int(round(float((B[1].split(':')[2])))) # round seconds to nearest integer
    timestamp = [year, month, date, hour, minute, second]
    return (timestamp)
    
