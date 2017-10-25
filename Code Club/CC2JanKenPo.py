'''
Created on Oct 25, 2017

@author: Bryson
'''
from random import randint
chosen=randint(1,3)
if chosen == 1:
    computer = 'rock'
elif chosen == 2:
    computer = 'paper'
elif chosen == 3:
    computer = 'scissors'
    
player = input('Select an action: rock (1), paper (2), or scissors (3)')
if player == 1:
    print('rock vs ' + computer)
elif player == 2:
    print('paper vs ' + computer)
elif player == 3:
    print ('scissors vs ' + computer)

if chosen == player:
    print('Draw')
elif chosen>player:
    print('Computer Wins')
elif chosen<player:
    print('You Win') 