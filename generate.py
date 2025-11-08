# generate.py
import pyrosim.pyrosim as pyrosim

def send_cube(name, x, y, z, lx, ly, lz):
    pyrosim.Send_Cube(
        name=name,
        pos=[x, y, z],
        size=[lx, ly, lz]
    )

def main():
    pyrosim.Start_SDF("boxes.sdf")

    #  single link with position variables
    length, width, height = 1.0, 1.0, 1.0
    x, y, z = 0.0, 0.0, height / 2.0  # bottom sits at z=0
    send_cube("Box", x, y, z, length, width, height)

    # --- second link (in front of and just above the first) ---
    # reset size to 1x1x1 per instructions
    length2, width2, height2 = 1.0, 1.0, 1.0
    gap = 0.01
    x2 = x                     # aligned in x
    y2 = y + width/2 + width2/2 + gap   # just in front
    z2 = height/2 + height2/2 + gap     # just above
    send_cube("Box2", x2, y2, z2, length2, width2, height2)

    # --- procedural tower(s) ---
    # parameters (reduce rows/cols/levels if your machine is older)
    rows, cols = 3, 3         # set >1 for a grid of towers (nested loops)
    levels = 10                # number of blocks per tower
    base = 1.0                 # base size (cubes start as 1m)
    scale = 0.9                # each level is 90% of the size below it
    spacing = 2.0              # gap between tower centers

    for r in range(rows):
        for c in range(cols):
            # tower base position
            tx = 2.5 + c * spacing   # shift towers away from the two initial boxes
            ty = 0.0 + r * spacing

            # cumulative height to place centers correctly
            cum_h = 0.0
            for k in range(levels):
                lx = base * (scale ** k)
                ly = base * (scale ** k)
                lz = base * (scale ** k)

                # center z for this block sits on top of the stack so far
                zc = cum_h + lz / 2.0
                send_cube(f"Tower_r{r}_c{c}_k{k}", tx, ty, zc, lx, ly, lz)

                cum_h += lz

    pyrosim.End()

if __name__ == "__main__":
    main()