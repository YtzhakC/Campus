import random


totalPoints = 1000000
pointsInCircle = 0

for i in range(totalPoints):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 <= 1:
        pointsInCircle += 1
        
pi_estimate = 4 * pointsInCircle / totalPoints
print(f"Estimado de pi: {pi_estimate}")
print(f"Puntos que cayeron en el círculo: {pointsInCircle:,}")
