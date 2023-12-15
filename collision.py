import numpy as np
from sympy import *

import math

# Generate random values for the given parameters
P_radar = np.array([1, 0])  # Random location of radar on the horizontal axis
P_launcher = np.array([10, 0])  # Random location of missile launcher on the horizontal axis
direction_enemy_missile = 60
direction_enemy_missile= math.radians(direction_enemy_missile)# Random direction of enemy missile
initial_distance_radar_enemy = 15 # Random initial distance between radar and enemy missile at t=0



C= math.sqrt(initial_distance_radar_enemy**2 - P_radar[0]**2)
m= math.tan(direction_enemy_missile)


alpha=math.acos(P_radar[0]/initial_distance_radar_enemy)
beta= 180 - math.degrees(alpha)
xp = Symbol('xp')
xp= solve(C**2 + xp**2-initial_distance_radar_enemy**2-(xp-P_radar[0])**2+(2*initial_distance_radar_enemy*(xp-P_radar[0])*math.cos(beta)),xp)
xp = xp[0]
yp=m*xp+C
m2=(yp-P_launcher[1])/(xp-P_launcher[0])
print (m2)
theta= math.atan(-m2)
theta= 180 - math.degrees(theta)
print(xp,yp,theta)
        
