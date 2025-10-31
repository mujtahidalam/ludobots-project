import pybullet as p
import time 

#connect the pysics server with GUI
physicsClient = p.connect(p.GUI)

p.loadSDF("box.sdf")

#run 1000 simulation steps
for i in range (1000):
    p.stepSimulation()
    print("Simulation step:", i)
    time.sleep(1/60) 
    
p.disconnect()