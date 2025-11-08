# simulate.py
import time
import pybullet as p
import pybullet_data

physicsClient = p.connect(p.GUI)                          # open GUI
p.setAdditionalSearchPath(pybullet_data.getDataPath()) # so plane.urdf resolves


p.setGravity(0, 0, -9.8)

plane_id = p.loadURDF("plane.urdf")                   # floor
p.loadSDF("boxes.sdf")                                  # generated box

# settle the scene a bit
p.setRealTimeSimulation(0)

#run 1000 simulation steps
for i in range (1000):
    p.stepSimulation()
    print("Simulation step:", i)
    time.sleep(1/60) 
    
p.disconnect()