'''
Created on Oct 25, 2017

@author: Bryson
'''
import random

players = ['Ali','Mike','Sean','Rachel','Jeonghwan','Bryson']

print('Current Squad:')
for i in range(6):
    print(players[i]) 
print(' ')

teamA = [] 
teamB = []

while len(players)>0:
    playerA = random.choice(players)
    #print(playerA)
    teamA.append(playerA) #Adds value to the end of object
    players.remove(playerA)
    #print('Players left:', players)

    playerB = random.choice(players)
    #print(playerB)
    teamB.append(playerB)
    players.remove(playerB)
    #print('Players left:', players)

print(' ')
print('Team Dinosaurs')
print(teamA)
print(' ')
print('Team Fellows Room')
print(teamB)