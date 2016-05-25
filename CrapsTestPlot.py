# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 18:46:19 2015

@author: Sig
"""

import numpy



'''
***************** Craps Array Functions*****************
'''

def rollDie(n):
    import random    
    die = random.randint(1,n)
    return die
    
def crapsRoll(): 
    a = rollDie(6)
    b = rollDie(6)
    c = a + b
    return(c)
    
def crapsStreak(score, goal, streakCount):
       if streakCount > 1:
           if score == goal:
               streakCount = 1
           elif score == 7:
               streakCount = 1            
           else:
               streakCount = streakCount + 1
       else:
           if score == 2 or score == 3 or score == 7 or score == 11 or score == 12:
               streakCount = 1
           else :
               streakCount = streakCount + 1
       return(streakCount)

def crapsScore(minBet, point, roll, bets):
    import pandas as pd

    bmat = pd.read_csv(bets, index_col = 'Bet')
    bmat['Units']=bmat['Units'].astype('float64')

    score = float(0.0)
    if point == 0 :  # Come out roll scores
        if roll == 7 or roll == 11 : 
            score = 1 * bmat.loc['pass', 'Units']
        # If shooter hits a Yo    
        if roll == 2 or roll == 3 or roll == 12 : 
            score = -1 * bmat.loc['pass', 'Units']
        # If shooter craps
    if point > 0 :

        if roll == 7 :
            # Simplify by removing if statements for combined losers 
            # but add complexity for not having bets out when a point is established
            betLoss = bmat.loc['pass','Units'] + bmat.loc['odds','Units'] + bmat.loc['place_4','Units'] + bmat.loc['place_5','Units'] + 1.2 * bmat.loc['place_6','Units'] + 1.2 * bmat.loc['place_8','Units'] + bmat.loc['place_9','Units'] + bmat.loc['place_10','Units'] + bmat.loc['field','Units'] 
            if (point == 6 and bmat.loc['place_6','Units'] > 0) or (point == 8 and bmat.loc['place_8','Units']) :
                betLoss = betLoss - 1.2
                # Subtract 1.2 unit if 6 or 8 is not placed while point
            if (point == 4 and bmat.loc['place_4','Units'] > 0) or (point == 10 and bmat.loc['place_10','Units']) : 
                betLoss = betLoss -1
                # Subtract 1 unit if 4 or 10 is not placed while point
            if (point == 5 and bmat.loc['place_5','Units'] > 0) or (point == 9 and bmat.loc['place_9','Units']) : 
                betLoss = betLoss -1
                # Subtract 1 unit if 5 or 9 is not placed while point  
            score= score - betLoss    
            #print (betLoss*minBet)

        if point == roll:
            if bmat.loc['pass','Units']>0 : #Pass bet is added
                score = score + bmat.loc['pass','Units']
            if bmat.loc['odds','Units']>0 : #Odds bet is added 
                if point == 4 or point == 10:
                    score = score +2 * bmat.loc['odds','Units']
                if point == 5 or point == 9 :
                    score = score + 1.5 * bmat.loc['odds','Units']
                if point == 6 or point == 8 :
                    score = score +1.2 * bmat.loc['odds','Units']
                if bmat.loc['field','Units'] > 0 and(point == 4 or point == 9 or point == 10 ) :  
                    score = score + bmat.loc['field','Units']

        if point != roll and point != 7:
            if roll == 2 :
                if bmat.loc['field','Units']>0 :
                    score = score + 2 * bmat.loc['field','Units']
                    print('2 pays double')
            if roll == 3 :
                if bmat.loc['field','Units']>0 :
                    score = score + bmat.loc['field','Units']
                    print('Field 3')
            if roll == 4 :
                if bmat.loc['field','Units']>0 :
                    score = score + bmat.loc['field','Units']
                    print('Field 4')
                if bmat.loc['place_4','Units']>0 :
                    score = score + 1.8 * bmat.loc['place_4','Units']
                    print('Place bet 4')    
            if roll == 5 :
                 if bmat.loc['field','Units']>0 :
                    score = score - bmat.loc['field','Units']
                    print('Field loses')
                 if bmat.loc['place_5','Units']>0 :
                    score = score + 1.4 * bmat.loc['place_5','Units']
                    print('Place bet 5') 
            if roll == 6 :
                 if bmat.loc['field','Units']>0 :
                    score = score - bmat.loc['field','Units']
                    print('Field loses')
                 if bmat.loc['place_6','Units']>0 :
                    score = score + 1.4 * bmat.loc['place_6','Units']
                    #Odds are actually 1.2 but I'm cheating to get to 6 pays 7
                    print('Place bet 6')  
            if roll == 8 :
                 if bmat.loc['field','Units']>0 :
                    score = score - bmat.loc['field','Units']
                    print('Field loses')
                 if bmat.loc['place_8','Units']>0 :
                    score = score + 1.4 * bmat.loc['place_8','Units']
                    #Odds are actually 1.2 but I'm cheating to get to 6 pays 7
                    print('Place bet 8')  
            if roll == 9 :
                 if bmat.loc['field','Units']>0 :
                    score = score + bmat.loc['field','Units']
                    print('Field 9')
                 if bmat.loc['place_9','Units']>0 :
                    score = score + 1.4 * bmat.loc['place_9','Units']
                    print('Place bet 9')
            if roll == 10 :
                if bmat.loc['field','Units']>0 :
                    score = score + bmat.loc['field','Units']
                    print('Field 10')
                if bmat.loc['place_10','Units']>0 :
                    score = score + 1.8 * bmat.loc['place_10','Units']
                    print('Place bet 10')        
            if roll == 11 :
                if bmat.loc['field','Units']>0 :
                    score = score + bmat.loc['field','Units']
                    print('Field 11')
            if roll == 12 :
                if bmat.loc['field','Units']>0 :
                    score = 2 * score + bmat.loc['field','Units']
                    print('12 scores double')        
                
    score = score * minBet 
    return(score)
   

       
def crapsArray(count, minBet, bankRoll) :   
    import numpy as np  
    import pandas as pd
    rollcount = 0
    inc = 0
    shooter = 1
    streak = 1 #Determines if Come Out roll
    point = 0
    rolls = []    
    row = []
    minBet = 5
    while inc < count:
        inc = inc + 1
        rollcount = rollcount + 1
        roll = crapsRoll()
        if streak > 1: #Evaluate rolls other than Come Out roll
            if roll == 7:
                print("7 - Craps!") 
                outcome = crapsScore(minBet, point, roll, '~/Python/Craps/Bet_Matrix.csv')
            elif point == roll:
                print("Winner!")
                outcome = crapsScore(minBet, point, roll, '~/Python/Craps/Bet_Matrix.csv')
            else:
                outcome = crapsScore(minBet, point, roll, '~/Python/Craps/Bet_Matrix.csv')
            
        else: #Evaluate Come Out roll
            if roll == 2:
                print("2 - Craps!")
                outcome = crapsScore(minBet, point, roll, '~/Python/Craps/Bet_Matrix.csv')
            elif roll == 3:  
                print("3 - Craps!")
                outcome = crapsScore(minBet, point, roll, '~/Python/Craps/Bet_Matrix.csv')
            elif roll == 7:
                print("7 - Yo!")
                outcome = crapsScore(minBet, point, roll, '~/Python/Craps/Bet_Matrix.csv')
            elif roll == 11:
                print("11 - Yo!")
                outcome = crapsScore(minBet, point, roll, '~/Python/Craps/Bet_Matrix.csv')
            elif roll == 12:
                print("12 - Craps!")
                outcome = crapsScore(minBet, point, roll, '~/Python/Craps/Bet_Matrix.csv')
            else:
                outcome = crapsScore(minBet, point, roll, '~/Python/Craps/Bet_Matrix.csv')
                point = roll              
        # Output results 
                 
                        
        bankRoll = bankRoll + outcome 
       
        
        row = [rollcount, roll, point, shooter, streak, outcome, bankRoll]
        rolls.append(row)
        pointTemp = point
        if roll == 7 and streak > 1:
            shooter = shooter + 1 
            point = 0
        elif roll == point and streak > 1:
            point = 0
        else:
            pass
        streak = crapsStreak(roll, pointTemp, streak)
        pointTemp=0

    else:
        print("Rolls Done")   
    rollsArray = np.asarray(rolls)
    numpy.savetxt('test.csv', rollsArray, fmt= '%3.0f', delimiter = ',', header = "roll,score,point,shooter,streak,value,bank", comments ='')    
    csv=pd.read_csv('test.csv')    
    return(csv)


# Function to write a list of Craps outcomes
def crapsMonteCarlo(sets, count, minBet, bankRoll) :
    import numpy as np
    import pandas as pd    
    
    #declare internal counter
    counter = 0
    output = []
    
    while(counter < sets):
        temp = crapsArray(count, minBet, bankRoll)
        output.append(temp)
        counter = counter + 1
        
   
    return(output)
    
#testing = []
testing = crapsMonteCarlo(10, 100, 5, 300)    
 
     
#numpy.savetxt('test.csv', temp, fmt= '%3.0f', delimiter = ',', header = "roll,score,point,shooter,streak,value,bank", comments ='')



'''
********************* Bokeh Plots ***********************
'''
import pandas as pd
from bokeh.charts import Bar, output_file, show, defaults
import bokeh.plotting as bp 
from bokeh.models import FixedTicker, LinearAxis
from bokeh.io import output_file, show, vplot

crapsArray(100, 5, 300)  
csv=pd.read_csv('test.csv')

output_file("craps.html")

#Plot sizes for charts
defaults.width = 1200
defaults.height = 300

action = Bar(csv, 'roll', values = 'score', title = "Craps Outcomes", bar_width = 1, color = 'score')
money = Bar(csv, 'roll', values = 'bank', title = "Craps Bankroll", bar_width = 1, color = 'score')
winLose = Bar(csv, 'roll', values = 'value', title = "Craps Roll Win/Loss", bar_width = 1, color = 'score')

xaxis=action.select({'type' : LinearAxis})
xaxis.ticker=FixedTicker(ticks=[0,25,50,75,100])
yaxis=action.select({'type' : LinearAxis})
yaxis.ticker=FixedTicker(ticks=[2,3,4,5,6,7,8,9,10,11,12])


p = vplot(action, money,winLose)

show(p)
print("Cashing Out")
