#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 17:38:46 2018

@author: Miranda

@contact: r03544029@ntu.edu.tw

README available on https://github.com/Mirandayaoyao/GPA-Calculator

A python-based lightweight calculator to convert GPA

INPUT:
    100-like score
    mode:        
        - std4
        - v1
        - v2
        - pku4
    
OUTPUT:
    4.0-like GPA

"""




''' 
    mapping function map 100 based score into 4.0 GPA
    INPUT:  mode - which version;   score - 100 based
    OUTPUT: output

'''


    

def gpaMap(mode, scoreList):
    output = None
    outputList = []
    
    for i in range(len(scoreList)):
        score = scoreList[i]
        
        if mode == "std4":
            if score <= 100 and score >= 90:
                output = 4.0
            elif score <= 89 and score >= 80:
                output = 3.0
            elif score <= 79 and score >= 70:
                output = 2.0
            elif score <= 69 and score >= 60:
                output = 1.0
            else:
                output = 0.0
    
                
        elif mode == "v1":
            if score <= 100 and score >= 85:
                output = 4.0
            elif score <= 84 and score >= 70:
                output = 3.0
            elif score <= 69 and score >= 60:
                output = 2.0
            else:
                output = 0.0
                
        elif mode == "v2":
            if score <= 100 and score >= 85:
                output = 4.0
            elif score <= 84 and score >= 75:
                output = 3.0
            elif score <= 74 and score >= 60:
                output = 2.0
            else:
                output = 0.0
                
        elif mode == "pku4":
            if score <= 100 and score >= 90:
                output = 4.0
            elif score <= 89 and score >= 85:
                output = 3.7
            elif score <= 84 and score >= 82:
                output = 3.3
            elif score <= 81 and score >= 78:
                output = 3.0
            elif score <= 77 and score >= 75:
                output = 2.7
            elif score <= 74 and score >= 72:
                output = 2.3
            elif score <= 71 and score >= 68:
                output = 2.0
            elif score <= 67 and score >= 64:
                output = 1.5
            elif score <= 63 and score >= 60:
                output = 1.0
            else:
                output = 0.0
                
        else:
            print("wrong mode setup")
            
        outputList.append(output)
                        
    return outputList

def weightedAverage(INPUT_SCORE,INPUT_CREDIT):
    Sum = 0
    SumC = 0
    for i in range(len(INPUT_SCORE)):
        Sum  += INPUT_SCORE[i] * INPUT_CREDIT[i]
        SumC += INPUT_CREDIT[i]
    return Sum * 1.0 / SumC



"=========================  MAIN SCRIPT ======================================"
# init
INPUT_SCORE  = [78, 64]
INPUT_CREDIT = [12,12]
MODE         = "pku4"
OUTPUT       = [ ]
Sum          = 0   # sum of weighted score
SumC         = 0  # sum of credit

if sum(INPUT_SCORE)/len(INPUT_SCORE) >= 5.0:
    INPUT_SCORE = gpaMap(MODE, INPUT_SCORE)
    print("mapped scores are %s"%INPUT_SCORE)
    
OUTPUT = weightedAverage(INPUT_SCORE,INPUT_CREDIT)
print("converted GPA %s"%OUTPUT)
    