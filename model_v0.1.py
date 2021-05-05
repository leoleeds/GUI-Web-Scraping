"""Import Libraries and Frameworks"""

#import random
#import operator
import matplotlib.pyplot
from agentframework import Agent
import time
import csv
import tkinter


"""Initial Setup and Parameters"""

#start = time.time() # start time counter

matplotlib.use('TkAgg') # ensure that TkInter is used
rowlist = [] # this creates an empty row list
environment=[] # this creates an empty environment list
num_of_agents = 100 # this limits the number of agents
num_of_iterations = 10
neighbourhood = 20
agents = [] # this creates an empty agents list


"""Environment CSV"""

f = open('in.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:
    rowlist = []
    environment.append(rowlist)
    for value in row:
        rowlist.append(value) # fill the environment list
        
f.close()


"""Verify that Environment has Imported Correctly"""

#matplotlib.pyplot.imshow(environment)
#matplotlib.pyplot.show()


"""Make the Agents"""

for i in range(num_of_agents): # this fills the list of agents
    agents.append(Agent(environment, agents, 2, 3))
    
    
"""Verify that Agents are added correctly"""

#print ("Initial coordinates")
#for i in range (num_of_agents):
#    print(agents[i].y, agents [i].x)
    

"""Define the Figure and Axes for Animation"""

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

    
"""Generate Animated Scatter Graph of Agents"""

def update(frame_number):
    fig.clear()
    """Call and Loop Through the Agents"""
    for j in range (num_of_iterations):
        for i in range (num_of_agents):
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)
    """Generate Scatter Graph of Agents"""
    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.imshow(environment)
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
#    matplotlib.pyplot.show()

animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, frames=num_of_iterations, repeat=False)


"""Run Model"""

def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, frames=num_of_iterations, repeat=False)
    canvas.draw()
    
    
"""Build the Canvas"""

root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


"""Create Menu"""

menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)
    
   
"""Verify Final Agents"""
#print("Final coordinates")
#for i in range (num_of_agents):
#    print(agents[i].y, agents[i].x)


"""Output to .CSV"""

f2 = open('output.csv','w',newline='')
writer = csv.writer(f2, delimiter = ' ')

for row in environment:
    writer.writerow(row)
f2.close()


"""Check Timing"""

#end = time.time() # end time counter
#print(end - start) # processing time in seconds


"""Await User Input"""

tkinter.mainloop() 