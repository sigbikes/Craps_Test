# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 18:46:19 2015

@author: Sig
"""

import numpy


'''cash = []
cash.append(300)'''


def rollDie(n):
    import random    
    die = random.randint(1,n)
    return die
    
def crapsRoll(): 
    a = rollDie(6)
    b = rollDie(6)
    c = a + b
    return(c)
    
def crapsArray(count) :   
    import numpy as np
   
    rollcount = 0
    inc = 0
    rolls = []
    row = []
    while inc < count:
        inc = inc + 1
        rollcount = rollcount + 1
        roll = crapsRoll()
        row = [rollcount, roll]
        rolls.append(row)     
    else:
        rollsArray = np.asarray(rolls)
        print(' Rolls Done')    
           
    return(rollsArray)


#minBet = 5
#point = 4
#roll = 4

#units = crapsScore(minBet, point, roll, '~/Python/Craps/Bet_Matrix.csv') 


'''temp = crapsArray(100)       
numpy.savetxt('test.csv', temp, fmt= '%3.0d', delimiter = ',', header = "roll,score", comments ='')
'''

print ('CrapsTest Complete')