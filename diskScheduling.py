#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 20180210
# V 0.1
# Auteur : AD
# LOOK and C-LOOK disk scheduling algorithms implementation

# random library required in order to generate the requests list
import random

class diskHead():
    def __init__ (self, position, direction, requests):
        self.position = position
        self.direction = direction
        self.requests = requests
        self.posIndex = requests.index(position)

    def moveTo (self, newPosition):
        # remove the request for the current position (we're here)
        self.requests.remove(self.position)
        # move to the new request position
        self.position = self.requests[newPosition]
        print("Reached position : ", self.position)

    def look (self):
        print('Starting LOOK/SCAN algorithm')
        #check that there are requests and loop through them
        while(self.requests):
            # sort the requests list (ascending order)
            self.requests.sort()
            # posIndex is the index of our position in the requests list
            self.posIndex = self.requests.index(self.position)

            # if we only have 1 request in our list
            if(len(self.requests) == 1):
                # remove the request and exit the program 
                # we are already at this position from our last movement
                self.requests.remove(self.position)
                break
            
            # head direction is up
            elif(self.direction == 'up'):
                # while there is still a request in the list, higher than our position
                while(self.posIndex < len(self.requests)-1):
                    self.moveTo(self.posIndex)
                else:
                    # no more request higher than our position
                    # we can now scan in the other direction
                    self.direction = 'down'
            
            # head direction is down
            else:
                # while we are not at the lowest request
                while(self.posIndex > 0):
                    # we go to the next request, descending order
                    self.posIndex -= 1
                    self.moveTo(self.posIndex)
                else:
                    # no requests left in this direction, inversing
                    self.direction = 'up'
        
        print('No requests, exiting')

    def clook (self):
        print('Starting C-LOOK algorithm')
        # check that there are requests and loop through them
        while (self.requests):
            # sort the requests list (ascending order)
            self.requests.sort()
            # posIndex is the index of our position in the requests list
            self.posIndex = self.requests.index(self.position)

            # while there is still a request in the list, higher than our position
            while (self.posIndex < len(self.requests)-1):
                self.moveTo(self.posIndex)
            
            # if we are at the last request in the list
            if (self.posIndex == len(self.requests)-1):
                # if that request is the only one
                if (self.posIndex == 0):
                    # we remove the request, we are alreay in position
                    print('last request', self.position, self.requests)
                    print('disk head to position 0')
                    self.requests.remove(self.position)
                    # we go back to position 0, waiting for requests
                    self.position = 0
                    break
                # multiples requests left
                else:
                    # remove the current request, we are in position
                    self.requests.remove(self.position)
                    # insert a request for position 0 at the start of the requests list
                    # this allow us to bring the disk head back to the beginning of the disk
                    self.requests.insert(0,0)
                    self.position = self.requests[0]
        
        print('No requests, exiting')

# randomized requests list, 50 requests
requestsList = []
requestsList2 = []
for x in range(0, 50): 
    requestsList.append(random.randint(0,200))
    requestsList2.append(random.randint(0,200))

# initialize our disk head with the random requests list
# determine our position using the first request in the list (non sorted)
dH = diskHead(requestsList[0], 'down', requestsList)
dH2 = diskHead(requestsList2[0], 'up', requestsList2)

# scan our requests list using LOOK/SCAN algorithm
dH.look()

# scan our requests list using C-LOOK algorithm
dH2.clook()