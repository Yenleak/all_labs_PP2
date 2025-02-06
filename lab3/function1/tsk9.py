
import math
def volume_0f_sphere(rad):
    V = (4/3)*math.pi*(rad**3)
    return V

radi = int(input("Radius: "))
res = volume_0f_sphere(radi)
print(f"Volume of sphere: {res}")