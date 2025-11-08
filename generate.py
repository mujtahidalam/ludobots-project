# generate.py
import pyrosim.pyrosim as pyrosim

def main():
    # set variables (start with 1,1,1; later set to 1,2,3)
    length, width, height = 1, 1, 3

    pyrosim.Start_SDF("box.sdf")
    pyrosim.Send_Cube(
        name="Box",
        pos=[0.0, 0.0, height / 2.0],  # spawn above ground by half its height
        size=[length, width, height]
    )
    pyrosim.End()

if __name__ == "__main__":
    main()
