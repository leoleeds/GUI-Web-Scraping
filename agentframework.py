"""Import Libraries and Frameworks"""

import random


"""Creat Agent Class and Definitions"""

class Agent():
    def __init__(self, environment, agents, x, y):
        self.environment=environment
        self.agents = agents
        self.store=0
        self.x=random.randint(0,99)
        self.y=random.randint(0,99)
                
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100

        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100    
            
    def eat(self): 
        if self.environment[self.y][self.x] > 10:
              self.environment[self.y][self.x] -= 10
              self.store += 10
              
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5 

    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            dist = self.distance_between(agent)
            if dist <= neighbourhood:
                sum = self.store + agent.store
                ave = sum /2
                self.store = ave
                agent.store = ave
                #print("sharing " + str(dist) + " " + str(ave))