from pyrosim.commonFunctions import Save_Whitespace

# pyrosim/geometrysdf.py
class GEOMETRY_SDF:
    def __init__(self, shape, size=None, radius=None, length=None):
        # normalize + alias
        shape = (shape or "").lower()
        if shape == "cube":
            shape = "box"

        self.shape = shape

        if shape == "box":
            L, W, H = size
            self.string1 = (
                "      <geometry>\n"
                "        <box>\n"
                f"          <size>{L} {W} {H}</size>"
            )
            self.string2 = (
                "\n"
                "        </box>\n"
                "      </geometry>"
            )

        elif shape == "sphere":
            r = radius
            self.string1 = (
                "      <geometry>\n"
                "        <sphere>\n"
                f"          <radius>{r}</radius>"
            )
            self.string2 = (
                "\n"
                "        </sphere>\n"
                "      </geometry>"
            )

        elif shape == "cylinder":
            r, L = radius, length
            self.string1 = (
                "      <geometry>\n"
                "        <cylinder>\n"
                f"          <radius>{r}</radius>\n"
                f"          <length>{L}</length>"
            )
            self.string2 = (
                "\n"
                "        </cylinder>\n"
                "      </geometry>"
            )
        else:
            raise ValueError(f"Unknown geometry shape: {shape}")

    def Save(self, f):
        f.write(self.string1 + "\n")
        f.write(self.string2 + "\n")