'''
Created on Oct 25, 2017

@author: Bryson
'''
import random

players = ['Ali','Mike','Sean','Rachel','Jeonghwan','Bryson', 'Andreas']

print('Current Squad:')
for i in range(7):
    print(players[i]) 
print(' ')

players.remove('Andreas')

teamA = [] 
teamB = []

print('Team Losers Who Don\'t Play Basketball')
print('[\'Andreas\']')

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
